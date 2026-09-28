"""
Core module for Py-GeoSpatial.

This module provides base classes, data structures, and fundamental abstractions
for all spatial data types.
"""

from pygeospatial.core.base import SpatialData, VectorData, RasterData, PointCloudData
from pygeospatial.core.crs import CRS
from pygeospatial.core.bounds import Bounds
from pygeospatial.core.metadata import Metadata

__all__ = [
    "SpatialData",
    "VectorData", 
    "RasterData",
    "PointCloudData",
    "CRS",
    "Bounds",
    "Metadata",
]
