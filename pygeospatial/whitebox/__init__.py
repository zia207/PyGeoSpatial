"""
WhiteboxTools integration module for Py-GeoSpatial.

This module provides integration with WhiteboxTools, giving access to 518+
specialized geospatial analysis tools with GPU acceleration support.
"""

from pygeospatial.whitebox.utils import WhiteboxToolsWrapper

# Create a global whitebox tools instance
_whitebox_instance = None


def get_whitebox_tools():
    """
    Get the global WhiteboxTools instance.
    
    Returns:
        WhiteboxToolsWrapper instance
    """
    global _whitebox_instance
    if _whitebox_instance is None:
        _whitebox_instance = WhiteboxToolsWrapper()
    return _whitebox_instance


# Dynamically create tool functions
def _create_tool_function(tool_name: str):
    """Create a function that calls a specific WhiteboxTool."""
    def tool_function(*args, **kwargs):
        wbt = get_whitebox_tools()
        return wbt.run_tool(tool_name, *args, **kwargs)
    
    tool_function.__name__ = tool_name
    tool_function.__doc__ = f"WhiteboxTools {tool_name} - See WhiteboxTools documentation for details."
    return tool_function


# Placeholder for tool functions - these will be dynamically generated
# when the full implementation is complete
# For now, we'll provide a few key examples

def slope(dem: str, output: str, **kwargs):
    """
    Calculate slope from DEM using WhiteboxTools.
    
    Args:
        dem: Input DEM file path
        output: Output slope raster path
        **kwargs: Additional parameters for slope calculation
    
    Returns:
        Output file path
    """
    wbt = get_whitebox_tools()
    return wbt.run_tool("slope", dem, output, **kwargs)


def aspect(dem: str, output: str, **kwargs):
    """
    Calculate aspect from DEM using WhiteboxTools.
    
    Args:
        dem: Input DEM file path
        output: Output aspect raster path
        **kwargs: Additional parameters for aspect calculation
    
    Returns:
        Output file path
    """
    wbt = get_whitebox_tools()
    return wbt.run_tool("aspect", dem, output, **kwargs)


def hillshade(dem: str, output: str, **kwargs):
    """
    Calculate hillshade from DEM using WhiteboxTools.
    
    Args:
        dem: Input DEM file path
        output: Output hillshade raster path
        **kwargs: Additional parameters for hillshade calculation
    
    Returns:
        Output file path
    """
    wbt = get_whitebox_tools()
    return wbt.run_tool("hillshade", dem, output, **kwargs)


def breach_depressions(dem: str, output: str, **kwargs):
    """
    Breach depressions in DEM using WhiteboxTools.
    
    Args:
        dem: Input DEM file path
        output: Output breached DEM path
        **kwargs: Additional parameters for depression breaching
    
    Returns:
        Output file path
    """
    wbt = get_whitebox_tools()
    return wbt.run_tool("breach_depressions", dem, output, **kwargs)


def d8_flow_accumulation(dem: str, output: str, **kwargs):
    """
    Calculate D8 flow accumulation using WhiteboxTools.
    
    Args:
        dem: Input DEM file path
        output: Output flow accumulation raster path
        **kwargs: Additional parameters for flow accumulation
    
    Returns:
        Output file path
    """
    wbt = get_whitebox_tools()
    return wbt.run_tool("d8_flow_accumulation", dem, output, **kwargs)


def watershed(flow_accum: str, pour_points: str, output: str, **kwargs):
    """
    Delineate watersheds using WhiteboxTools.
    
    Args:
        flow_accum: Flow accumulation raster path
        pour_points: Pour points file path
        output: Output watershed raster path
        **kwargs: Additional parameters for watershed delineation
    
    Returns:
        Output file path
    """
    wbt = get_whitebox_tools()
    return wbt.run_tool("watershed", flow_accum, pour_points, output, **kwargs)


def lidar_ground_point_filter(input_las: str, output_las: str, **kwargs):
    """
    Filter ground points from LiDAR data using WhiteboxTools.
    
    Args:
        input_las: Input LAS file path
        output_las: Output LAS file path with ground points
        **kwargs: Additional parameters for ground filtering
    
    Returns:
        Output file path
    """
    wbt = get_whitebox_tools()
    return wbt.run_tool("lidar_ground_point_filter", input_las, output_las, **kwargs)


def lidar_tin_gridding(input_las: str, output_raster: str, **kwargs):
    """
    Generate raster from LiDAR points using TIN gridding with WhiteboxTools.
    
    Args:
        input_las: Input LAS file path
        output_raster: Output raster file path
        **kwargs: Additional parameters for TIN gridding
    
    Returns:
        Output file path
    """
    wbt = get_whitebox_tools()
    return wbt.run_tool("lidar_tin_gridding", input_las, output_raster, **kwargs)


__all__ = [
    "get_whitebox_tools",
    "slope",
    "aspect", 
    "hillshade",
    "breach_depressions",
    "d8_flow_accumulation",
    "watershed",
    "lidar_ground_point_filter",
    "lidar_tin_gridding",
]
