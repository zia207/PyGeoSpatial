"""
Spatial bounds and extent management.

This module provides functionality for managing spatial bounds and extents
of geographic datasets.
"""

from typing import Tuple, Optional
import math


class Bounds:
    """
    Spatial bounds representation.
    
    This class represents the spatial extent (bounding box) of geographic data
    with methods for bounds calculations and manipulations.
    """
    
    def __init__(self, minx: float, miny: float, maxx: float, maxy: float):
        """
        Initialize bounds.
        
        Args:
            minx: Minimum x coordinate
            miny: Minimum y coordinate
            maxx: Maximum x coordinate
            maxy: Maximum y coordinate
        
        Raises:
            ValueError: If bounds are invalid (min > max)
        """
        if minx > maxx or miny > maxy:
            raise ValueError(f"Invalid bounds: minx ({minx}) > maxx ({maxx}) or miny ({miny}) > maxy ({maxy})")
        
        self._minx = float(minx)
        self._miny = float(miny)
        self._maxx = float(maxx)
        self._maxy = float(maxy)
    
    @property
    def minx(self) -> float:
        """Minimum x coordinate."""
        return self._minx
    
    @property
    def miny(self) -> float:
        """Minimum y coordinate."""
        return self._miny
    
    @property
    def maxx(self) -> float:
        """Maximum x coordinate."""
        return self._maxx
    
    @property
    def maxy(self) -> float:
        """Maximum y coordinate."""
        return self._maxy
    
    @property
    def width(self) -> float:
        """Width of bounds (maxx - minx)."""
        return self._maxx - self._minx
    
    @property
    def height(self) -> float:
        """Height of bounds (maxy - miny)."""
        return self._maxy - self._miny
    
    @property
    def area(self) -> float:
        """Area of bounds."""
        return self.width * self.height
    
    @property
    def centroid(self) -> Tuple[float, float]:
        """Centroid of bounds."""
        return ((self._minx + self._maxx) / 2, (self._miny + self._maxy) / 2)
    
    def to_tuple(self) -> Tuple[float, float, float, float]:
        """
        Convert bounds to tuple.
        
        Returns:
            Tuple of (minx, miny, maxx, maxy)
        """
        return (self._minx, self._miny, self._maxx, self._maxy)
    
    def to_list(self) -> list:
        """
        Convert bounds to list.
        
        Returns:
            List of [minx, miny, maxx, maxy]
        """
        return [self._minx, self._miny, self._maxx, self._maxy]
    
    def __str__(self) -> str:
        """String representation."""
        return f"Bounds({self._minx}, {self._miny}, {self._maxx}, {self._maxy})"
    
    def __repr__(self) -> str:
        """Detailed string representation."""
        return f"Bounds(minx={self._minx}, miny={self._miny}, maxx={self._maxx}, maxy={self._maxy})"
    
    def __eq__(self, other) -> bool:
        """Check bounds equality."""
        if not isinstance(other, Bounds):
            return False
        return (self._minx == other._minx and self._miny == other._miny and
                self._maxx == other._maxx and self._maxy == other._maxy)
    
    def __contains__(self, point: Tuple[float, float]) -> bool:
        """
        Check if point is within bounds.
        
        Args:
            point: Tuple of (x, y) coordinates
        
        Returns:
            True if point is within bounds
        """
        x, y = point
        return (self._minx <= x <= self._maxx and self._miny <= y <= self._maxy)
    
    def intersects(self, other: "Bounds") -> bool:
        """
        Check if bounds intersect with another bounds.
        
        Args:
            other: Other bounds to check intersection with
        
        Returns:
            True if bounds intersect
        """
        return not (self._maxx < other._minx or self._minx > other._maxx or
                   self._maxy < other._miny or self._miny > other._maxy)
    
    def intersection(self, other: "Bounds") -> Optional["Bounds"]:
        """
        Calculate intersection with another bounds.
        
        Args:
            other: Other bounds to intersect with
        
        Returns:
            Intersection bounds, or None if no intersection
        """
        if not self.intersects(other):
            return None
        
        minx = max(self._minx, other._minx)
        miny = max(self._miny, other._miny)
        maxx = min(self._maxx, other._maxx)
        maxy = min(self._maxy, other._maxy)
        
        return Bounds(minx, miny, maxx, maxy)
    
    def union(self, other: "Bounds") -> "Bounds":
        """
        Calculate union with another bounds.
        
        Args:
            other: Other bounds to union with
        
        Returns:
            Union bounds
        """
        minx = min(self._minx, other._minx)
        miny = min(self._miny, other._miny)
        maxx = max(self._maxx, other._maxx)
        maxy = max(self._maxy, other._maxy)
        
        return Bounds(minx, miny, maxx, maxy)
    
    def buffer(self, distance: float) -> "Bounds":
        """
        Buffer bounds by specified distance.
        
        Args:
            distance: Buffer distance (can be negative)
        
        Returns:
            Buffered bounds
        """
        return Bounds(
            self._minx - distance,
            self._miny - distance,
            self._maxx + distance,
            self._maxy + distance
        )
    
    @classmethod
    def from_points(cls, points: list) -> "Bounds":
        """
        Create bounds from list of points.
        
        Args:
            points: List of (x, y) coordinate tuples
        
        Returns:
            Bounds encompassing all points
        """
        if not points:
            raise ValueError("Cannot create bounds from empty point list")
        
        x_coords = [p[0] for p in points]
        y_coords = [p[1] for p in points]
        
        return cls(
            min(x_coords),
            min(y_coords),
            max(x_coords),
            max(y_coords)
        )
    
    @classmethod
    def from_extent(cls, extent: Tuple[float, float, float, float]) -> "Bounds":
        """
        Create bounds from extent tuple.
        
        Args:
            extent: Tuple of (minx, miny, maxx, maxy)
        
        Returns:
            Bounds object
        """
        return cls(*extent)
