"""
WhiteboxTools integration examples for Py-GeoSpatial.

This script demonstrates how to use WhiteboxTools through the Py-GeoSpatial interface.
"""

import pygeospatial as pg
from pygeospatial.whitebox import get_whitebox_tools

# Example 1: Basic WhiteboxTools usage
print("Example 1: Basic WhiteboxTools Usage")
try:
    wbt = get_whitebox_tools()
    print(f"WhiteboxTools wrapper created: {wbt}")
    
    # Try to get version if WhiteboxTools is available
    try:
        version = wbt.version()
        print(f"WhiteboxTools version: {version}")
    except RuntimeError as e:
        print(f"Note: {e}")
        print("WhiteboxTools executable not found - install with: pip install whitebox")
    
except Exception as e:
    print(f"Error: {e}")
print()

# Example 2: Using WhiteboxTools functions
print("Example 2: Using WhiteboxTools Functions")
print("Note: These functions require actual data files and WhiteboxTools installation")
print()

# Example terrain analysis (requires DEM file)
print("Terrain Analysis Example:")
print("  slope = pg.whitebox.slope('dem.tif', 'slope.tif')")
print("  aspect = pg.whitebox.aspect('dem.tif', 'aspect.tif')")
print("  hillshade = pg.whitebox.hillshade('dem.tif', 'hillshade.tif')")
print()

# Example hydrological analysis (requires DEM file)
print("Hydrological Analysis Example:")
print("  filled = pg.whitebox.breach_depressions('dem.tif', 'filled.tif')")
print("  flow_accum = pg.whitebox.d8_flow_accumulation('filled.tif', 'flow.tif')")
print("  watersheds = pg.whitebox.watershed('flow.tif', 'pour_points.shp', 'watersheds.tif')")
print()

# Example LiDAR processing (requires LAS file)
print("LiDAR Processing Example:")
print("  ground = pg.whitebox.lidar_ground_point_filter('input.las', 'ground.las')")
print("  dtm = pg.whitebox.lidar_tin_gridding('ground.las', 'dtm.tif')")
print()

# Example 3: WhiteboxTools with GPU acceleration
print("Example 3: WhiteboxTools with GPU Acceleration")
print("with pg.gpu_backend():")
print("    result = pg.whitebox.slope('large_dem.tif', 'slope.tif')")
print()

# Example 4: Setting WhiteboxTools options
print("Example 4: Setting WhiteboxTools Options")
try:
    wbt = get_whitebox_tools()
    wbt.set_verbose(True)
    wbt.set_gpu_enabled(True)
    wbt.set_num_workers(4)
    print("WhiteboxTools options configured:")
    print(f"  Verbose: {wbt._verbose}")
    print(f"  GPU enabled: {wbt._use_gpu}")
    print(f"  Num workers: {wbt._num_workers}")
except Exception as e:
    print(f"Error: {e}")
print()

print("WhiteboxTools integration examples completed!")
print("Note: Most examples require actual data files and WhiteboxTools installation")
