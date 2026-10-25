# RGB to YCbCr

Compares a floating-point conversion with a fixed-coefficient integer approximation. OpenCV loads color images as BGR, so the script converts to RGB before applying either formula.

```bash
python rgb-to-ycbcr/convert.py path/to/image.jpg
```

Creates separate grayscale `Y`, `Cb`, and `Cr` PNGs for both methods in `output/`. A three-channel YCbCr array is not saved as a normal RGB picture because ordinary image viewers would interpret its channels incorrectly. Adapted from the two course conversion scripts.
