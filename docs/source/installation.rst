Installation
============

Requirements
------------

Py-GeoSpatial requires Python 3.9 or higher.

Core Dependencies
~~~~~~~~~~~~~~~~~

* NumPy >= 1.21.0
* SciPy >= 1.7.0
* Pandas >= 1.3.0
* Shapely >= 1.8.0
* GDAL >= 3.3.0
* PyProj >= 3.2.0

Basic Installation
------------------

Install from PyPI::

    pip install pygeospatial

Install from source::

    git clone https://github.com/yourusername/Py-GeoSpatial.git
    cd Py-GeoSpatial
    pip install -e .

Optional Dependencies
---------------------

I/O Support
~~~~~~~~~~~

For enhanced I/O capabilities::

    pip install pygeospatial[io]

This includes:
* Rasterio >= 1.2.0
* Fiona >= 1.8.0
* GeoPandas >= 0.10.0

GPU/Compute Support
~~~~~~~~~~~~~~~~~~~

For GPU acceleration and parallel computing::

    pip install pygeospatial[compute]

This includes:
* CuPy >= 10.0.0
* Numba >= 0.56.0
* Dask >= 2021.10.0

Visualization
~~~~~~~~~~~~~

For visualization capabilities::

    pip install pygeospatial[viz]

This includes:
* Matplotlib >= 3.5.0
* Plotly >= 5.0.0
* Folium >= 0.12.0
* PyVista >= 0.35.0

WhiteboxTools Integration
~~~~~~~~~~~~~~~~~~~~~~~~~~

For WhiteboxTools integration::

    pip install pygeospatial[whitebox]

This includes:
* Whitebox >= 2.0.0

All Optional Dependencies
~~~~~~~~~~~~~~~~~~~~~~~~~~

To install all optional dependencies::

    pip install pygeospatial[all]

Development Installation
------------------------

For development::

    git clone https://github.com/yourusername/Py-GeoSpatial.git
    cd Py-GeoSpatial
    pip install -e .[dev]

This will install the package in development mode along with development tools:
* pytest >= 7.0.0
* pytest-cov >= 3.0.0
* black >= 22.0.0
* flake8 >= 4.0.0
* mypy >= 0.950
* sphinx >= 4.5.0
* sphinx-rtd-theme >= 1.0.0

Verifying Installation
----------------------

To verify your installation::

    python -c "import pygeospatial; print(pygeospatial.__version__)"

You should see the version number printed.
