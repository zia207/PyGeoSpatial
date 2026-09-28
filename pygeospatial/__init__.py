"""
Py-GeoSpatial: Comprehensive geospatial analysis package with multi-core CPU and GPU support.

This package provides a unified interface for vector, raster, and point cloud data processing
with native support for multi-core CPU and GPU acceleration.
"""

__version__ = "0.1.0"
__author__ = "Py-GeoSpatial Contributors"
__license__ = "MIT"

# Import main API components
from pygeospatial.api import (
    read_vector,
    read_raster,
    read_pointcloud,
    gpu_backend,
    cpu_backend,
)

# Import configuration
from pygeospatial.api.config import config

__all__ = [
    "read_vector",
    "read_raster",
    "read_pointcloud",
    "gpu_backend",
    "cpu_backend",
    "config",
]
