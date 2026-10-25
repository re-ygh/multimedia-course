# Global SSIM

Calculates structural similarity from the luminance, contrast, and covariance of two grayscale images. This implementation produces one **global** score; it does not average scores over local windows like the common library implementation.

```bash
python ssim/ssim.py path/to/original.jpg path/to/comparison.jpg
```

Images must have equal dimensions. Identical images give a score of 1. Adapted from the university `ex3/main.py` exercise; the formula and input handling have been corrected.
