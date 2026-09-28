"""
Compute module for Py-GeoSpatial.

This module provides CPU and GPU compute backends for spatial operations.
"""

from pygeospatial.compute.backend import (
    ComputeBackend,
    CPUBackend,
    GPUBackend,
    BackendManager,
    get_backend_manager,
)

__all__ = [
    "ComputeBackend",
    "CPUBackend",
    "GPUBackend",
    "BackendManager",
    "get_backend_manager",
]
