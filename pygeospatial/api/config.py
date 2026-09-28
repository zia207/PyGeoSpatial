"""
Configuration management for Py-GeoSpatial.

This module provides global configuration settings for backends, performance,
and other package-level options.
"""

import threading
from contextlib import contextmanager
from typing import Optional


class Config:
    """Global configuration manager for Py-GeoSpatial."""
    
    def __init__(self):
        self._backend = "cpu"  # Default to CPU backend
        self._num_workers = None  # None means auto-detect
        self._cache_size = "1GB"
        self._log_level = "INFO"
        self._lock = threading.Lock()
    
    @property
    def backend(self) -> str:
        """Get current compute backend."""
        return self._backend
    
    def set_backend(self, backend: str) -> None:
        """
        Set compute backend.
        
        Args:
            backend: Either 'cpu' or 'gpu'
        """
        if backend not in ["cpu", "gpu"]:
            raise ValueError(f"Backend must be 'cpu' or 'gpu', got '{backend}'")
        
        # Try to initialize GPU backend if requested
        if backend == "gpu":
            from pygeospatial.compute import get_backend_manager
            backend_manager = get_backend_manager()
            if not backend_manager.initialize_gpu():
                raise RuntimeError("GPU backend is not available. Install GPU dependencies: pip install pygeospatial[compute]")
            backend_manager.set_backend("gpu")
        else:
            from pygeospatial.compute import get_backend_manager
            backend_manager = get_backend_manager()
            backend_manager.set_backend("cpu")
        
        with self._lock:
            self._backend = backend
    
    @property
    def num_workers(self) -> Optional[int]:
        """Get number of worker processes."""
        return self._num_workers
    
    def set_num_workers(self, num_workers: Optional[int]) -> None:
        """
        Set number of worker processes for parallel operations.
        
        Args:
            num_workers: Number of workers, or None for auto-detect
        """
        if num_workers is not None and num_workers < 1:
            raise ValueError("num_workers must be >= 1 or None")
        
        with self._lock:
            self._num_workers = num_workers
        
        # Update CPU backend if available
        from pygeospatial.compute import get_backend_manager
        backend_manager = get_backend_manager()
        if num_workers is not None:
            backend_manager.cpu_backend.set_num_workers(num_workers)
    
    @property
    def cache_size(self) -> str:
        """Get cache size."""
        return self._cache_size
    
    def set_cache_size(self, cache_size: str) -> None:
        """
        Set cache size for result caching.
        
        Args:
            cache_size: Cache size as string (e.g., '1GB', '512MB')
        """
        with self._lock:
            self._cache_size = cache_size
    
    @property
    def log_level(self) -> str:
        """Get logging level."""
        return self._log_level
    
    def set_log_level(self, log_level: str) -> None:
        """
        Set logging level.
        
        Args:
            log_level: Logging level ('DEBUG', 'INFO', 'WARNING', 'ERROR')
        """
        valid_levels = ["DEBUG", "INFO", "WARNING", "ERROR"]
        if log_level not in valid_levels:
            raise ValueError(f"log_level must be one of {valid_levels}, got '{log_level}'")
        with self._lock:
            self._log_level = log_level
    
    def get_backend_info(self) -> dict:
        """
        Get information about available backends.
        
        Returns:
            Dictionary with backend information
        """
        from pygeospatial.compute import get_backend_manager
        backend_manager = get_backend_manager()
        return backend_manager.get_backend_info()


# Global configuration instance
config = Config()


@contextmanager
def gpu_backend():
    """
    Context manager to temporarily use GPU backend.
    
    Example:
        with pg.gpu_backend():
            result = large_raster.complex_operation()
    """
    previous_backend = config.backend
    config.set_backend("gpu")
    try:
        yield
    finally:
        config.set_backend(previous_backend)


@contextmanager
def cpu_backend():
    """
    Context manager to temporarily use CPU backend.
    
    Example:
        with pg.cpu_backend():
            result = operation.prefer_cpu()
    """
    previous_backend = config.backend
    config.set_backend("cpu")
    try:
        yield
    finally:
        config.set_backend(previous_backend)
