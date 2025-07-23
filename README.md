<div align="center">
  <a href="./README.md"><strong>English</strong></a> | <a href="./README.ru.md">Русский</a>
</div>
<hr>

# Pixel-Canon

> The canon for pixel data topology. A cross-language specification to define the logical layout of images (axis order, orientation, and memory order).

`Pixel-Canon` is a cross-language project aimed at solving a common and frustrating problem in computer vision and machine learning: the ambiguity of image data layouts. Is it `(Height, Width, Channels)` or `(Channels, Height, Width)`? Does the Y-axis point up or down?

This project provides a simple, declarative specification and a set of tools to describe this information explicitly, eliminating guesswork and making data pipelines more robust.

## The Specification

The formal specification, which all language-specific implementations must adhere to, can be found here:
*   **[Specification v1.0](./spec/v1.0.md)**

## Implementations

### **[Python](./python/)** (`pixel-canon` on PyPI)

The Python implementation is available and includes a backend for `numpy`.

**Installation:**
```bash
# Core library
pip install pixel-canon

# With NumPy support
pip install "pixel-canon[numpy]"
```

**Example Usage:**
```python
import numpy as np
from pixel_canon import CommonLayouts
from pixel_canon.backends.numpy_backend import convert_numpy

# Image from OpenCV (HWC, BGR)
# NOTE: OpenCV uses BGR, but we'll use an RGB layout for this example.
image_hwc = np.zeros((480, 640, 3), dtype=np.uint8)
layout_hwc = CommonLayouts.HWC_ROW_MAJOR_RGB

# Target layout for a PyTorch model (CHW, RGB)
layout_chw = CommonLayouts.CHW_ROW_MAJOR_RGB

# Safely convert the layout
image_chw = convert_numpy(image_hwc, src=layout_hwc, dst=layout_chw)

print(f"Original shape: {image_hwc.shape}")
print(f"Converted shape: {image_chw.shape}")
# Original shape: (480, 640, 3)
# Converted shape: (3, 480, 640)
```

### *Other Languages*
Implementations for Rust, TypeScript, Java, and other languages are planned. Contributions are welcome!

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.
