# Multimedia Coursework | تمرین‌های چندرسانه‌ای

A curated collection of image-processing exercises from my university multimedia course. Each exercise has its own folder, short explanation, and command. The examples accept an image supplied by the reader; no course images or local Python environment are committed.

مجموعه‌ای از تمرین‌های منتخب درس چندرسانه‌ای. هر تمرین پوشه و راهنمای جدا دارد و تصویر ورودی را از کاربر می‌گیرد.

## Exercises

| Folder | Topic | Output |
| --- | --- | --- |
| [bit-plane-slicing](bit-plane-slicing/) | Extract eight grayscale bit planes | Eight PNG files |
| [rgb-to-ycbcr](rgb-to-ycbcr/) | Float and integer RGB to YCbCr conversion | Y, Cb, Cr channel images |
| [averaging-filter](averaging-filter/) | 3×3 uniform smoothing filter | Filtered PNG |
| [image-resizing](image-resizing/) | Upscaling and downscaling | Two PNG files |
| [ssim](ssim/) | Global grayscale structural similarity | Score in terminal |

## Setup

Requires Python 3 and the packages in `requirements.txt`:

```bash
python -m venv .venv
python -m pip install -r requirements.txt
```

Activate the virtual environment using the command for your operating system, then run an exercise from this repository's root. Example:

```bash
python bit-plane-slicing/bit_planes.py path/to/image.jpg
```

Commands that write files use `output/` by default. It is ignored by Git. Pass `--output` to choose another directory.

## Scope

These are educational implementations. The SSIM exercise computes one score over the whole image, rather than a sliding-window score. The original course folder also contained an ImageNet/CIFAR-10 comparison that directly compared incompatible class labels; it is excluded because its reported accuracy would be misleading.
