"""
Core components of the Pixel-Canon specification.

This module contains the fundamental building blocks for describing image layouts,
including Enums for axes and their properties, and the main ImageLayout dataclass.
"""
from dataclasses import dataclass
from enum import Enum, auto
from typing import Tuple, Dict, Final

class ImageAxis(Enum):
    """Represents a named, logical axis of the image data."""
    HEIGHT = auto()
    WIDTH = auto()
    CHANNELS = auto()
    DEPTH = auto()

class AxisDirection(Enum):
    """Represents the semantic direction of a spatial axis."""
    DOWN = auto()
    UP = auto()
    RIGHT = auto()
    LEFT = auto()
    FORWARD = auto()
    BACKWARD = auto()
    SYMMETRIC = auto()

class ChannelFormat:
    """
    Represents the semantic meaning and order of channels.
    Using a class with constants instead of an Enum for easy string representation.
    """
    RGB: Final[str] = "RGB"
    RGBA: Final[str] = "RGBA"
    BGR: Final[str] = "BGR"
    BGRA: Final[str] = "BGRA"
    LUMINANCE: Final[str] = "LUMINANCE" # Using a full word for clarity
    ALPHA: Final[str] = "ALPHA"

class MemoryOrder(Enum):
    """Defines how logical axes map to linear memory."""
    ROW_MAJOR = auto()    # C-style: last axis is fastest
    COLUMN_MAJOR = auto() # Fortran-style: first axis is fastest

@dataclass(frozen=True, eq=True)
class ImageLayout:
    """
    A complete, unambiguous description of an image's logical layout.
    
    This object is immutable and hashable, so it can be used as a dictionary key.
    """
    axis_order: Tuple[ImageAxis, ...]
    memory_order: MemoryOrder
    channels: str # Using str type hint for compatibility with ChannelFormat constants
    directions: Dict[ImageAxis, AxisDirection]
