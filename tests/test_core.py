"""
Tests for core module.
"""

import pytest
from pygeospatial.core import CRS, Bounds, Metadata


class TestCRS:
    """Test CRS functionality."""
    
    def test_crs_from_epsg(self):
        """Test creating CRS from EPSG code."""
        crs = CRS.from_epsg(4326)
        assert str(crs) == "EPSG:4326"
    
    def test_crs_from_string(self):
        """Test creating CRS from string."""
        crs = CRS("EPSG:4326")
        assert str(crs) == "EPSG:4326"
    
    def test_crs_from_int(self):
        """Test creating CRS from integer."""
        crs = CRS(4326)
        assert str(crs) == "EPSG:4326"
    
    def test_crs_equality(self):
        """Test CRS equality."""
        crs1 = CRS.from_epsg(4326)
        crs2 = CRS.from_epsg(4326)
        assert crs1 == crs2
    
    def test_crs_to_epsg(self):
        """Test extracting EPSG code."""
        crs = CRS.from_epsg(4326)
        assert crs.to_epsg() == 4326
    
    def test_crs_is_geographic(self):
        """Test geographic CRS detection."""
        crs = CRS.from_epsg(4326)
        assert crs.is_geographic
        assert not crs.is_projected


class TestBounds:
    """Test Bounds functionality."""
    
    def test_bounds_creation(self):
        """Test creating bounds."""
        bounds = Bounds(0, 0, 10, 10)
        assert bounds.minx == 0
        assert bounds.miny == 0
        assert bounds.maxx == 10
        assert bounds.maxy == 10
    
    def test_bounds_properties(self):
        """Test bounds properties."""
        bounds = Bounds(0, 0, 10, 10)
        assert bounds.width == 10
        assert bounds.height == 10
        assert bounds.area == 100
        assert bounds.centroid == (5, 5)
    
    def test_bounds_invalid(self):
        """Test invalid bounds raise error."""
        with pytest.raises(ValueError):
            Bounds(10, 10, 0, 0)
    
    def test_bounds_contains(self):
        """Test point containment."""
        bounds = Bounds(0, 0, 10, 10)
        assert (5, 5) in bounds
        assert (15, 15) not in bounds
    
    def test_bounds_intersects(self):
        """Test bounds intersection."""
        bounds1 = Bounds(0, 0, 10, 10)
        bounds2 = Bounds(5, 5, 15, 15)
        assert bounds1.intersects(bounds2)
        
        bounds3 = Bounds(20, 20, 30, 30)
        assert not bounds1.intersects(bounds3)
    
    def test_bounds_intersection(self):
        """Test bounds intersection calculation."""
        bounds1 = Bounds(0, 0, 10, 10)
        bounds2 = Bounds(5, 5, 15, 15)
        intersection = bounds1.intersection(bounds2)
        assert intersection.minx == 5
        assert intersection.miny == 5
        assert intersection.maxx == 10
        assert intersection.maxy == 10
    
    def test_bounds_union(self):
        """Test bounds union."""
        bounds1 = Bounds(0, 0, 10, 10)
        bounds2 = Bounds(5, 5, 15, 15)
        union = bounds1.union(bounds2)
        assert union.minx == 0
        assert union.miny == 0
        assert union.maxx == 15
        assert union.maxy == 15
    
    def test_bounds_buffer(self):
        """Test bounds buffering."""
        bounds = Bounds(0, 0, 10, 10)
        buffered = bounds.buffer(5)
        assert buffered.minx == -5
        assert buffered.miny == -5
        assert buffered.maxx == 15
        assert buffered.maxy == 15
    
    def test_bounds_from_points(self):
        """Test creating bounds from points."""
        points = [(0, 0), (10, 10), (5, 5)]
        bounds = Bounds.from_points(points)
        assert bounds.minx == 0
        assert bounds.miny == 0
        assert bounds.maxx == 10
        assert bounds.maxy == 10


class TestMetadata:
    """Test Metadata functionality."""
    
    def test_metadata_creation(self):
        """Test creating metadata."""
        metadata = Metadata()
        assert metadata.created is not None
        assert metadata.modified is not None
    
    def test_metadata_attributes(self):
        """Test custom attributes."""
        metadata = Metadata()
        metadata.set_attribute("key", "value")
        assert metadata.get_attribute("key") == "value"
        assert metadata.get_attribute("nonexistent", "default") == "default"
    
    def test_metadata_quality(self):
        """Test quality indicators."""
        metadata = Metadata()
        metadata.set_quality_indicator("accuracy", 0.95)
        assert metadata.get_quality_indicator("accuracy") == 0.95
    
    def test_metadata_provenance(self):
        """Test provenance tracking."""
        metadata = Metadata()
        metadata.add_provenance_entry("buffer", {"distance": 100})
        provenance = metadata.provenance
        assert len(provenance) == 1
        assert provenance[0]["operation"] == "buffer"
    
    def test_metadata_to_dict(self):
        """Test metadata serialization."""
        metadata = Metadata()
        metadata.set_attribute("key", "value")
        data = metadata.to_dict()
        assert "attributes" in data
        assert data["attributes"]["key"] == "value"
    
    def test_metadata_to_json(self):
        """Test metadata JSON serialization."""
        metadata = Metadata()
        metadata.set_attribute("key", "value")
        json_str = metadata.to_json()
        assert "key" in json_str
        assert "value" in json_str
