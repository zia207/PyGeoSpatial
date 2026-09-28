Quick Start Guide
================

This guide will help you get started with Py-GeoSpatial quickly.

Basic Concepts
--------------

Py-GeoSpatial provides a unified interface for working with different types of spatial data:

* **Vector Data**: Points, lines, and polygons (e.g., Shapefile, GeoJSON)
* **Raster Data**: Grid-based data (e.g., GeoTIFF, HDF5)
* **Point Cloud Data**: 3D point clouds (e.g., LAS, LAZ)

Configuration
-------------

Py-GeoSpatial can be configured for optimal performance:

.. code-block:: python

    import pygeospatial as pg

    # Set compute backend
    pg.config.set_backend("gpu")  # or "cpu"

    # Set number of parallel workers
    pg.config.set_num_workers(8)

    # Set cache size
    pg.config.set_cache_size("4GB")

    # Set logging level
    pg.config.set_log_level("INFO")

Loading Data
------------

Vector Data
~~~~~~~~~~~

.. code-block:: python

    import pygeospatial as pg

    # Load vector data
    vector_data = pg.read_vector("path/to/shapefile.shp")

    # Access properties
    print(f"CRS: {vector_data.crs}")
    print(f"Bounds: {vector_data.bounds}")
    print(f"Geometry type: {vector_data.geometry_type}")

Raster Data
~~~~~~~~~~~

.. code-block:: python

    # Load raster data
    raster_data = pg.read_raster("path/to/raster.tif")

    # Access properties
    print(f"Shape: {raster_data.shape}")
    print(f"Resolution: {raster_data.resolution}")
    print(f"NoData value: {raster_data.nodata}")

Point Cloud Data
~~~~~~~~~~~~~~~~

.. code-block:: python

    # Load point cloud data
    pointcloud = pg.read_pointcloud("path/to/points.las")

    # Access properties
    print(f"Number of points: {pointcloud.num_points}")
    print(f"CRS: {pointcloud.crs}")

Basic Operations
----------------

Vector Operations
~~~~~~~~~~~~~~~~

.. code-block:: python

    # Buffer geometries
    buffered = vector_data.buffer(100)

    # Intersection
    intersection = vector_data.intersect(other_vector)

    # Union
    union = vector_data.union(other_vector)

Raster Operations
~~~~~~~~~~~~~~~~~

.. code-block:: python

    # Calculate slope
    slope = raster_data.slope()

    # Calculate aspect
    aspect = raster_data.aspect()

    # Calculate hillshade
    hillshade = raster_data.hillshade()

Point Cloud Operations
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    # Filter ground points
    ground_points = pointcloud.filter_ground()

    # Generate digital terrain model
    dtm = pointcloud.generate_dtm()

GPU Acceleration
----------------

Py-GeoSpatial supports GPU acceleration for many operations:

.. code-block:: python

    # Use GPU backend for specific operations
    with pg.gpu_backend():
        result = large_raster.complex_operation()

    # Or set globally
    pg.config.set_backend("gpu")
    result = large_raster.complex_operation()

WhiteboxTools Integration
------------------------

Py-GeoSpatial provides seamless integration with WhiteboxTools:

.. code-block:: python

    # Terrain analysis
    slope = pg.whitebox.slope("dem.tif", "slope.tif")
    aspect = pg.whitebox.aspect("dem.tif", "aspect.tif")

    # Hydrological analysis
    filled = pg.whitebox.breach_depressions("dem.tif", "filled.tif")
    flow_accum = pg.whitebox.d8_flow_accumulation("filled.tif", "flow.tif")

    # LiDAR processing
    ground = pg.whitebox.lidar_ground_point_filter("input.las", "ground.las")
    dtm = pg.whitebox.lidar_tin_gridding("ground.las", "dtm.tif")

Saving Results
-------------

.. code-block:: python

    # Save vector data
    buffered.to_file("output.shp")

    # Save raster data
    slope.to_file("slope.tif")

    # Save point cloud data
    ground_points.to_file("ground.las")

Next Steps
----------

* Explore the :doc:`api/index` for detailed API documentation
* Check out the :doc:`examples/index` for more examples
* Learn about :doc:`whitebox/index` for WhiteboxTools integration
* Read the full :doc:`installation` guide for advanced setup options
