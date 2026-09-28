Py-GeoSpatial Documentation
=============================

Welcome to Py-GeoSpatial, a comprehensive, high-performance Python package for geospatial data processing and analysis with native support for multi-core CPU and GPU acceleration.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   installation
   quickstart
   api/index
   examples/index
   whitebox/index

Features
--------

* **Unified API**: Single interface for vector, raster, and point cloud data
* **Performance**: Multi-core CPU and GPU acceleration for all operations
* **Extensibility**: Plugin architecture for custom algorithms
* **Interoperability**: Seamless integration with GDAL, PROJ, and other geospatial libraries
* **WhiteboxTools Integration**: Access to 518+ specialized geospatial analysis tools
* **Modern Python**: Full type hints, async support, and Python 3.9+ compatibility

Installation
------------

Basic Installation::

    pip install pygeospatial

With GPU Support::

    pip install pygeospatial[compute]

With All Optional Dependencies::

    pip install pygeospatial[all]

Quick Start
-----------

.. code-block:: python

    import pygeospatial as pg

    # Load data
    vector_data = pg.read_vector("path/to/shapefile.shp")
    raster_data = pg.read_raster("path/to/raster.tif")

    # Perform operations
    buffered = vector_data.buffer(100)
    slope = raster_data.slope()

    # GPU acceleration
    with pg.gpu_backend():
        result = large_raster.complex_operation()

WhiteboxTools Integration
-------------------------

.. code-block:: python

    # Access WhiteboxTools through unified API
    with pg.gpu_backend():
        # Terrain analysis
        slope = pg.whitebox.slope("dem.tif", "slope.tif")
        aspect = pg.whitebox.aspect("dem.tif", "aspect.tif")

        # Hydrological analysis
        filled_dem = pg.whitebox.breach_depressions("dem.tif", "filled.tif")
        flow_accum = pg.whitebox.d8_flow_accumulation("filled.tif", "flow.tif")

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
