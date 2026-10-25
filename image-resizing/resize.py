"""Create enlarged and reduced versions of an image."""

import argparse
from pathlib import Path

import cv2


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("image", type=Path, help="Input image")
    parser.add_argument("--output", type=Path, default=Path("output"))
    args = parser.parse_args()

    image = cv2.imread(str(args.image), cv2.IMREAD_UNCHANGED)
    if image is None:
        parser.error(f"Cannot read image: {args.image}")
    height, width = image.shape[:2]
    args.output.mkdir(parents=True, exist_ok=True)
    for label, factor, interpolation in (
        ("enlarged", 2.0, cv2.INTER_LINEAR),
        ("reduced", 0.5, cv2.INTER_AREA),
    ):
        size = (max(1, round(width * factor)), max(1, round(height * factor)))
        path = args.output / f"{label}.png"
        if not cv2.imwrite(str(path), cv2.resize(image, size, interpolation=interpolation)):
            raise OSError(f"Cannot write {path}")
        print(path)


if __name__ == "__main__":
    main()
