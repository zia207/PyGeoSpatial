WhiteboxTools Integration
=========================

Py-GeoSpatial provides seamless integration with WhiteboxTools, giving you access to 518+ specialized geospatial analysis tools with GPU acceleration support.

Overview
--------

WhiteboxTools is an advanced geospatial data analysis platform developed by Prof. John Lindsay. Py-GeoSpatial integrates these tools into a unified Python interface with performance enhancements.

Key Features:

* **518+ Specialized Tools**: Access to the complete WhiteboxTools library
* **GPU Acceleration**: WhiteboxTools operations accelerated through GPU backends
* **Unified API**: Consistent interface with native Py-GeoSpatial data structures
* **Performance Optimization**: Parallel processing and memory optimization
* **Research-Grade Algorithms**: Academically validated algorithms for terrain analysis, hydrology, and LiDAR processing

Installation
------------

To use WhiteboxTools integration, install the whitebox package::

    pip install whitebox

Or install Py-GeoSpatial with WhiteboxTools support::

    pip install pygeospatial[whitebox]

Basic Usage
-----------

Terrain Analysis
~~~~~~~~~~~~~~~~

.. code-block:: python

    import pygeospatial as pg

    # Calculate slope
    slope = pg.whitebox.slope("dem.tif", "slope.tif")

    # Calculate aspect
    aspect = pg.whitebox.aspect("dem.tif", "aspect.tif")

    # Generate hillshade
    hillshade = pg.whitebox.hillshade("dem.tif", "hillshade.tif")

Hydrological Analysis
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    # Breach depressions in DEM
    filled = pg.whitebox.breach_depressions("dem.tif", "filled.tif")

    # Calculate flow accumulation
    flow_accum = pg.whitebox.d8_flow_accumulation("filled.tif", "flow.tif")

    # Delineate watersheds
    watersheds = pg.whitebox.watershed("flow.tif", "pour_points.shp", "watersheds.tif")

LiDAR Processing
~~~~~~~~~~~~~~~~

.. code-block:: python

    # Filter ground points
    ground = pg.whitebox.lidar_ground_point_filter("input.las", "ground.las")

    # Generate DTM from ground points
    dtm = pg.whitebox.lidar_tin_gridding("ground.las", "dtm.tif")

GPU Acceleration
----------------

WhiteboxTools operations can be accelerated using GPU:

.. code-block:: python

    # Use GPU backend for WhiteboxTools operations
    with pg.gpu_backend():
        slope = pg.whitebox.slope("large_dem.tif", "slope.tif")
        aspect = pg.whitebox.aspect("large_dem.tif", "aspect.tif")

Available Tools
---------------

Py-GeoSpatial provides access to all WhiteboxTools categories:

Data Tools
~~~~~~~~~~

* Format conversion and data cleaning
* Vector/raster operations
* Attribute table management

Geomorphometric Analysis
~~~~~~~~~~~~~~~~~~~~~~~~

* Terrain analysis (slope, aspect, curvature)
* Multi-scale topographic analysis
* Surface roughness and texture analysis

GIS Analysis
~~~~~~~~~~~~

* Spatial operations and interpolation
* Geometric analysis
* Spatial indexing

Hydrological Analysis
~~~~~~~~~~~~~~~~~~~~~

* Flow routing algorithms (D8, D-infinity, FD8, Rho8)
* Watershed delineation
* Depression handling

Image Processing
~~~~~~~~~~~~~~~~

* Remote sensing operations
* Change detection
* Image classification and enhancement

LiDAR Analysis
~~~~~~~~~~~~~

* Point cloud processing
* Ground point classification
* Surface generation

Mathematical and Statistical Analysis
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Statistical operations
* Mathematical functions
* Image correlation and regression

Precision Agriculture
~~~~~~~~~~~~~~~~~~~~~~

* Yield analysis
* Crop management tools

Stream Network Analysis
~~~~~~~~~~~~~~~~~~~~~~~

* Stream ordering
* Network analysis
* Longitudinal profiling

Advanced Configuration
----------------------

WhiteboxTools Wrapper Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    from pygeospatial.whitebox import get_whitebox_tools

    wbt = get_whitebox_tools()

    # Set working directory
    wbt.set_working_dir("/path/to/data")

    # Enable verbose output
    wbt.set_verbose(True)

    # Enable GPU acceleration
    wbt.set_gpu_enabled(True)

    # Set number of parallel workers
    wbt.set_num_workers(4)

Getting Tool Help
~~~~~~~~~~~~~~~~~

.. code-block:: python

    wbt = get_whitebox_tools()

    # Get help for a specific tool
    help_text = wbt.tool_help("slope")
    print(help_text)

    # List available tools
    tools = wbt.list_tools()
    print(tools)

    # List tools with keyword
    slope_tools = wbt.list_tools("slope")
    print(slope_tools)

Performance Considerations
---------------------------

* **GPU Acceleration**: Use GPU backend for large datasets and computationally intensive operations
* **Parallel Processing**: Set appropriate number of workers for your system
* **Memory Management**: Use chunked processing for very large datasets
* **Caching**: Enable result caching for repeated operations

For more information on WhiteboxTools, see the `WhiteboxTools User Manual <https://jblindsay.github.io/wbt_book/available_tools/index.html>`_.
