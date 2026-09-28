# Py-GeoSpatial

A comprehensive, high-performance Python package for geospatial data processing and analysis with native support for multi-core CPU and GPU acceleration.

## Features

- **Unified API**: Single interface for vector, raster, and point cloud data
- **Performance**: Multi-core CPU and GPU acceleration for all operations
- **Extensibility**: Plugin architecture for custom algorithms
- **Interoperability**: Seamless integration with GDAL, PROJ, and other geospatial libraries
- **WhiteboxTools Integration**: Access to 518+ specialized geospatial analysis tools
- **Modern Python**: Full type hints, async support, and Python 3.9+ compatibility

## Installation

### Basic Installation

```bash
pip install pygeospatial
```

### With GPU Support

```bash
pip install pygeospatial[compute]
```

### With All Optional Dependencies

```bash
pip install pygeospatial[all]
```

### Development Installation

```bash
git clone https://github.com/yourusername/Py-GeoSpatial.git
cd Py-GeoSpatial
pip install -e .[dev]
```

## Quick Start

```python
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
```

## WhiteboxTools Integration

```python
# Access WhiteboxTools through unified API
with pg.gpu_backend():
    # Terrain analysis
    slope = pg.whitebox.slope("dem.tif", "slope.tif")
    aspect = pg.whitebox.aspect("dem.tif", "aspect.tif")

    # Hydrological analysis
    filled_dem = pg.whitebox.breach_depressions("dem.tif", "filled.tif")
    flow_accum = pg.whitebox.d8_flow_accumulation("filled.tif", "flow.tif")
```

## Documentation

Full documentation is available at [https://Py-GeoSpatial.readthedocs.io](https://Py-GeoSpatial.readthedocs.io)

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

Contributions are welcome! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

## Acknowledgments

- Built on top of excellent geospatial libraries: GDAL, PROJ, Shapely, Rasterio, Fiona
- Integrated with [WhiteboxTools](https://github.com/jblindsay/whitebox-tools) for advanced geospatial analysis
- Inspired by the geospatial Python community
