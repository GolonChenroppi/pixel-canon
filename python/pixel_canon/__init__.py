"""
Pixel-Canon: A universal specification for describing image memory layouts.
"""
from .core import (
    ImageAxis,
    AxisDirection,
    ChannelFormat,
    MemoryOrder,
    ImageLayout
)
from .common import CommonLayouts

__version__ = "0.1.0"

__all__ = [
    "ImageAxis",
    "AxisDirection",
    "ChannelFormat",
    "MemoryOrder",
    "ImageLayout",
    "CommonLayouts",
    "__version__",
]
