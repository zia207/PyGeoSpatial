"""
Quick start functions for Py-GeoSpatial.

This module provides simplified functions for common geospatial operations.
"""

from typing import Union
from pathlib import Path


def read_vector(path: Union[str, Path]) -> "VectorData":
    """
    Read vector data from file.
    
    Args:
        path: Path to vector file (Shapefile, GeoJSON, etc.)
    
    Returns:
        VectorData object containing the loaded data
    
    Example:
        >>> vector_data = pg.read_vector("path/to/shapefile.shp")
        >>> buffered = vector_data.buffer(100)
    """
    from pygeospatial.vector import VectorData
    return VectorData.from_file(path)


def read_raster(path: Union[str, Path]) -> "RasterData":
    """
    Read raster data from file.
    
    Args:
        path: Path to raster file (GeoTIFF, etc.)
    
    Returns:
        RasterData object containing the loaded data
    
    Example:
        >>> raster_data = pg.read_raster("path/to/raster.tif")
        >>> slope = raster_data.slope()
    """
    from pygeospatial.raster import RasterData
    return RasterData.from_file(path)


def read_pointcloud(path: Union[str, Path]) -> "PointCloudData":
    """
    Read point cloud data from file.
    
    Args:
        path: Path to point cloud file (LAS, LAZ, etc.)
    
    Returns:
        PointCloudData object containing the loaded data
    
    Example:
        >>> pointcloud = pg.read_pointcloud("path/to/points.las")
        >>> dtm = pointcloud.generate_dtm()
    """
    from pygeospatial.pointcloud import PointCloudData
    return PointCloudData.from_file(path)
