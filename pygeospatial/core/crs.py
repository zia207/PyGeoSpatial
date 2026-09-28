"""
Coordinate reference system management.

This module provides functionality for managing coordinate reference systems (CRS)
and coordinate transformations.
"""

from typing import Optional, Union
import re


class CRS:
    """
    Coordinate reference system representation.
    
    This class wraps coordinate reference system information and provides
    methods for CRS validation and transformation.
    """
    
    def __init__(self, crs_string: Union[str, int]):
        """
        Initialize CRS from string or EPSG code.
        
        Args:
            crs_string: CRS definition (EPSG code, WKT string, or PROJ string)
        
        Examples:
            >>> crs = CRS("EPSG:4326")  # WGS84
            >>> crs = CRS(4326)  # Same as above
            >>> crs = CRS("PROJCS[...]")  # WKT string
        """
        if isinstance(crs_string, int):
            self._crs_string = f"EPSG:{crs_string}"
        else:
            self._crs_string = crs_string
        
        self._validate_crs()
    
    def _validate_crs(self) -> None:
        """Validate CRS string format."""
        # Basic validation - in production, this would use PROJ/GDAL
        if not self._crs_string:
            raise ValueError("CRS string cannot be empty")
        
        # Check for common patterns
        if not re.match(r'^(EPSG:\d+|PROJCS|GEOGCS|\+proj=)', self._crs_string):
            # Still accept it, but warn in production
            pass
    
    def __str__(self) -> str:
        """String representation of CRS."""
        return self._crs_string
    
    def __repr__(self) -> str:
        """Detailed string representation."""
        return f"CRS('{self._crs_string}')"
    
    def __eq__(self, other) -> bool:
        """Check CRS equality."""
        if not isinstance(other, CRS):
            return False
        return self._crs_string == other._crs_string
    
    def __hash__(self) -> int:
        """Hash for use in sets and dicts."""
        return hash(self._crs_string)
    
    @property
    def is_geographic(self) -> bool:
        """
        Check if CRS is geographic (lat/lon).
        
        Returns:
            True if geographic coordinate system
        """
        # Basic check - in production, use PROJ
        return "GEOGCS" in self._crs_string.upper() or "EPSG:4326" in self._crs_string
    
    @property
    def is_projected(self) -> bool:
        """
        Check if CRS is projected.
        
        Returns:
            True if projected coordinate system
        """
        return not self.is_geographic
    
    def to_epsg(self) -> Optional[int]:
        """
        Extract EPSG code if available.
        
        Returns:
            EPSG code as integer, or None if not available
        """
        match = re.search(r'EPSG:(\d+)', self._crs_string)
        if match:
            return int(match.group(1))
        return None
    
    @classmethod
    def from_epsg(cls, epsg_code: int) -> "CRS":
        """
        Create CRS from EPSG code.
        
        Args:
            epsg_code: EPSG code (e.g., 4326 for WGS84)
        
        Returns:
            CRS object
        """
        return cls(epsg_code)
    
    @classmethod
    def from_wkt(cls, wkt_string: str) -> "CRS":
        """
        Create CRS from WKT string.
        
        Args:
            wkt_string: Well-Known Text representation
        
        Returns:
            CRS object
        """
        return cls(wkt_string)
    
    @classmethod
    def from_proj4(cls, proj4_string: str) -> "CRS":
        """
        Create CRS from PROJ.4 string.
        
        Args:
            proj4_string: PROJ.4 string
        
        Returns:
            CRS object
        """
        return cls(proj4_string)
