"""Compare floating point and integer RGB to YCbCr conversions."""

import argparse
from pathlib import Path

import cv2
import numpy as np


def floating_point(rgb: np.ndarray) -> np.ndarray:
    channels = rgb.astype(np.float64) / 255.0
    r, g, b = channels[..., 0], channels[..., 1], channels[..., 2]
    y = 0.299 * r + 0.587 * g + 0.114 * b
    cb = 0.5 * (b - y) / 0.886 + 0.5
    cr = 0.5 * (r - y) / 0.701 + 0.5
    return np.clip(np.stack((y, cb, cr), axis=-1) * 255, 0, 255).astype(np.uint8)


def integer(rgb: np.ndarray) -> np.ndarray:
    channels = rgb.astype(np.int32)
    r, g, b = channels[..., 0], channels[..., 1], channels[..., 2]
    y = (299 * r + 587 * g + 114 * b) // 1000
    cb = (-1687 * r - 3313 * g + 5000 * b) // 10000 + 128
    cr = (5000 * r - 4187 * g - 813 * b) // 10000 + 128
    return np.clip(np.stack((y, cb, cr), axis=-1), 0, 255).astype(np.uint8)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("image", type=Path, help="Input color image")
    parser.add_argument("--output", type=Path, default=Path("output"))
    args = parser.parse_args()

    bgr = cv2.imread(str(args.image), cv2.IMREAD_COLOR)
    if bgr is None:
        parser.error(f"Cannot read image: {args.image}")
    rgb = cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB)
    args.output.mkdir(parents=True, exist_ok=True)
    for method, converted in (("float", floating_point(rgb)), ("integer", integer(rgb))):
        # Save channels separately: a YCbCr array is not an ordinary RGB image.
        for index, channel in enumerate(("Y", "Cb", "Cr")):
            path = args.output / f"{method}_{channel}.png"
            if not cv2.imwrite(str(path), converted[..., index]):
                raise OSError(f"Cannot write {path}")
            print(path)


if __name__ == "__main__":
    main()
