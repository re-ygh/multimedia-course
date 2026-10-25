"""Calculate global grayscale SSIM between two images."""

import argparse
from pathlib import Path

import cv2
import numpy as np


def global_ssim(first: np.ndarray, second: np.ndarray) -> float:
    if first.shape != second.shape:
        raise ValueError("Images must have the same dimensions")
    if first.size < 2:
        raise ValueError("Images must contain at least two pixels")

    x, y = first.astype(np.float64) / 255.0, second.astype(np.float64) / 255.0
    mu_x, mu_y = x.mean(), y.mean()
    var_x, var_y = x.var(ddof=1), y.var(ddof=1)
    covariance = ((x - mu_x) * (y - mu_y)).sum() / (x.size - 1)
    c1, c2 = 0.01**2, 0.03**2
    return float(
        ((2 * mu_x * mu_y + c1) * (2 * covariance + c2))
        / ((mu_x**2 + mu_y**2 + c1) * (var_x + var_y + c2))
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("original", type=Path)
    parser.add_argument("comparison", type=Path)
    args = parser.parse_args()

    images = [cv2.imread(str(path), cv2.IMREAD_GRAYSCALE) for path in (args.original, args.comparison)]
    if any(image is None for image in images):
        parser.error("Cannot read one or both input images")
    try:
        print(f"Global SSIM: {global_ssim(images[0], images[1]):.4f}")
    except ValueError as error:
        parser.error(str(error))


if __name__ == "__main__":
    main()
