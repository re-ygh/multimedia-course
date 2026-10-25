"""Apply a 3 by 3 uniform averaging kernel to an image."""

import argparse
from pathlib import Path

import cv2
import numpy as np
from scipy import ndimage


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("image", type=Path, help="Input image")
    parser.add_argument("--output", type=Path, default=Path("output"))
    args = parser.parse_args()

    image = cv2.imread(str(args.image), cv2.IMREAD_COLOR)
    if image is None:
        parser.error(f"Cannot read image: {args.image}")
    kernel = np.ones((3, 3), dtype=np.float64) / 9.0
    filtered = np.stack(
        [ndimage.convolve(image[..., channel].astype(np.float64), kernel, mode="reflect")
         for channel in range(3)],
        axis=-1,
    )
    args.output.mkdir(parents=True, exist_ok=True)
    path = args.output / "averaged.png"
    if not cv2.imwrite(str(path), np.clip(filtered, 0, 255).astype(np.uint8)):
        raise OSError(f"Cannot write {path}")
    print(path)


if __name__ == "__main__":
    main()
