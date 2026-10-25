"""Save the eight bit planes of a grayscale image."""

import argparse
from pathlib import Path

import cv2


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("image", type=Path, help="Input image")
    parser.add_argument("--output", type=Path, default=Path("output"))
    args = parser.parse_args()

    image = cv2.imread(str(args.image), cv2.IMREAD_GRAYSCALE)
    if image is None:
        parser.error(f"Cannot read image: {args.image}")

    args.output.mkdir(parents=True, exist_ok=True)
    for bit in range(7, -1, -1):
        plane = ((image >> bit) & 1) * 255
        path = args.output / f"bit_{bit}.png"
        if not cv2.imwrite(str(path), plane):
            raise OSError(f"Cannot write {path}")
        print(path)


if __name__ == "__main__":
    main()
