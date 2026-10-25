# Bit-plane slicing

Splits an 8-bit grayscale image into eight binary layers. Bit 7 contains the most significant information; bit 0 contains the least.

```bash
python bit-plane-slicing/bit_planes.py path/to/image.jpg
```

Creates `output/bit_7.png` through `output/bit_0.png`. Input can be any image OpenCV can read; it is converted to grayscale first. This is adapted from the university `8bit_grayscale.py` exercise.
