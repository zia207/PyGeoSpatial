"""
Base classes for spatial data types.

This module provides abstract base classes and fundamental data structures
for all spatial data types in Py-GeoSpatial.
"""

from abc import ABC, abstractmethod
from typing import Any, Dict, Optional, Union
from pathlib import Path

from pygeospatial.core.crs import CRS
from pygeospatial.core.bounds import Bounds
from pygeospatial.core.metadata import Metadata


class SpatialData(ABC):
    """
    Abstract base class for all spatial data types.
    
    This class provides the fundamental interface that all spatial data types
    must implement, including coordinate reference system management, bounds
    calculation, and metadata handling.
    """
    
    def __init__(self, crs: Optional[CRS] = None, metadata: Optional[Metadata] = None):
        """
        Initialize spatial data.
        
        Args:
            crs: Coordinate reference system
            metadata: Metadata about the dataset
        """
        self._crs = crs
        self._metadata = metadata or Metadata()
        self._bounds: Optional[Bounds] = None
    
    @property
    def crs(self) -> Optional[CRS]:
        """Get coordinate reference system."""
        return self._crs
    
    @crs.setter
    def crs(self, value: CRS) -> None:
        """Set coordinate reference system."""
        self._crs = value
        self._bounds = None  # Invalidate cached bounds
    
    @property
    def metadata(self) -> Metadata:
        """Get metadata."""
        return self._metadata
    
    @property
    @abstractmethod
    def bounds(self) -> Bounds:
        """Get spatial bounds."""
        pass
    
    @abstractmethod
    def to_file(self, path: Union[str, Path], **kwargs) -> None:
        """
        Save data to file.
        
        Args:
            path: Output file path
            **kwargs: Additional format-specific options
        """
        pass
    
    @classmethod
    @abstractmethod
    def from_file(cls, path: Union[str, Path], **kwargs) -> "SpatialData":
        """
        Load data from file.
        
        Args:
            path: Input file path
            **kwargs: Additional format-specific options
        
        Returns:
            Loaded spatial data object
        """
        pass
    
    def reproject(self, target_crs: CRS) -> "SpatialData":
        """
        Reproject data to different coordinate reference system.
        
        Args:
            target_crs: Target coordinate reference system
        
        Returns:
            Reprojected spatial data
        """
        raise NotImplementedError("Reprojection not implemented for this data type")
    
    def transform(self, **kwargs) -> "SpatialData":
        """
        Apply coordinate transformation.
        
        Args:
            **kwargs: Transformation parameters
        
        Returns:
            Transformed spatial data
        """
        raise NotImplementedError("Transformation not implemented for this data type")


class VectorData(SpatialData):
    """
    Base class for vector spatial data.
    
    This class represents vector data (points, lines, polygons) and provides
    the interface for vector-specific operations.
    """
    
    def __init__(self, crs: Optional[CRS] = None, metadata: Optional[Metadata] = None):
        super().__init__(crs, metadata)
        self._geometry_type: Optional[str] = None
    
    @property
    def geometry_type(self) -> Optional[str]:
        """Get geometry type (Point, LineString, Polygon, etc.)."""
        return self._geometry_type
    
    @abstractmethod
    def buffer(self, distance: float, **kwargs) -> "VectorData":
        """
        Buffer geometries by specified distance.
        
        Args:
            distance: Buffer distance
            **kwargs: Additional buffer parameters
        
        Returns:
            Buffered vector data
        """
        pass
    
    @abstractmethod
    def intersect(self, other: "VectorData") -> "VectorData":
        """
        Calculate intersection with another vector dataset.
        
        Args:
            other: Other vector dataset
        
        Returns:
            Intersection result
        """
        pass
    
    @abstractmethod
    def union(self, other: "VectorData") -> "VectorData":
        """
        Calculate union with another vector dataset.
        
        Args:
            other: Other vector dataset
        
        Returns:
            Union result
        """
        pass


class RasterData(SpatialData):
    """
    Base class for raster spatial data.
    
    This class represents raster data (grids) and provides the interface for
    raster-specific operations.
    """
    
    def __init__(self, crs: Optional[CRS] = None, metadata: Optional[Metadata] = None):
        super().__init__(crs, metadata)
        self._shape: Optional[tuple] = None
        self._resolution: Optional[tuple] = None
        self._nodata: Optional[float] = None
    
    @property
    def shape(self) -> Optional[tuple]:
        """Get raster shape (rows, columns)."""
        return self._shape
    
    @property
    def resolution(self) -> Optional[tuple]:
        """Get raster resolution (x, y)."""
        return self._resolution
    
    @property
    def nodata(self) -> Optional[float]:
        """Get NoData value."""
        return self._nodata
    
    @abstractmethod
    def slope(self, **kwargs) -> "RasterData":
        """
        Calculate slope from elevation data.
        
        Args:
            **kwargs: Additional slope parameters
        
        Returns:
            Slope raster
        """
        pass
    
    @abstractmethod
    def aspect(self, **kwargs) -> "RasterData":
        """
        Calculate aspect from elevation data.
        
        Args:
            **kwargs: Additional aspect parameters
        
        Returns:
            Aspect raster
        """
        pass


class PointCloudData(SpatialData):
    """
    Base class for point cloud spatial data.
    
    This class represents 3D point cloud data (LiDAR, etc.) and provides the
    interface for point cloud-specific operations.
    """
    
    def __init__(self, crs: Optional[CRS] = None, metadata: Optional[Metadata] = None):
        super().__init__(crs, metadata)
        self._num_points: Optional[int] = None
    
    @property
    def num_points(self) -> Optional[int]:
        """Get number of points."""
        return self._num_points
    
    @abstractmethod
    def filter_ground(self, **kwargs) -> "PointCloudData":
        """
        Filter ground points from point cloud.
        
        Args:
            **kwargs: Additional filtering parameters
        
        Returns:
            Ground point cloud
        """
        pass
    
    @abstractmethod
    def generate_dtm(self, **kwargs) -> "RasterData":
        """
        Generate digital terrain model.
        
        Args:
            **kwargs: Additional DTM generation parameters
        
        Returns:
            DTM raster
        """
        pass
