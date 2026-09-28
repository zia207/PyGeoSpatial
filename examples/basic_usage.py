"""
Basic usage examples for Py-GeoSpatial.

This script demonstrates basic usage of the Py-GeoSpatial package.
"""

import pygeospatial as pg

# Example 1: Configuration
print("Example 1: Configuration")
print(f"Default backend: {pg.config.backend}")
pg.config.set_backend("gpu")
print(f"Updated backend: {pg.config.backend}")
pg.config.set_backend("cpu")  # Reset to CPU
print()

# Example 2: CRS handling
print("Example 2: CRS Handling")
from pygeospatial.core import CRS

crs = CRS.from_epsg(4326)  # WGS84
print(f"CRS: {crs}")
print(f"Is geographic: {crs.is_geographic}")
print(f"EPSG code: {crs.to_epsg()}")
print()

# Example 3: Bounds
print("Example 3: Bounds")
from pygeospatial.core import Bounds

bounds = Bounds(0, 0, 10, 10)
print(f"Bounds: {bounds}")
print(f"Width: {bounds.width}, Height: {bounds.height}")
print(f"Area: {bounds.area}")
print(f"Centroid: {bounds.centroid}")
print()

# Example 4: Metadata
print("Example 4: Metadata")
from pygeospatial.core import Metadata

metadata = Metadata()
metadata.set_attribute("source", "USGS")
metadata.set_attribute("resolution", "30m")
metadata.set_quality_indicator("accuracy", 0.95)
metadata.add_provenance_entry("import", {"format": "GeoTIFF"})

print(f"Attributes: {metadata.attributes}")
print(f"Quality: {metadata.quality}")
print(f"Provenance entries: {len(metadata.provenance)}")
print()

# Example 5: Context managers
print("Example 5: Backend Context Managers")
print(f"Initial backend: {pg.config.backend}")

with pg.gpu_backend():
    print(f"Inside GPU context: {pg.config.backend}")

print(f"After GPU context: {pg.config.backend}")
print()

print("Basic usage examples completed successfully!")
