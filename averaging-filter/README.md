# Uniform averaging filter

Convolves each color channel with a 3×3 kernel whose weights are all 1/9. Reflective border handling avoids a dark frame caused by padding with zeroes.

```bash
python averaging-filter/average.py path/to/image.jpg
```

Creates `output/averaged.png`. Adapted from the university `UniformAveragingFilter.py` exercise.
