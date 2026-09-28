"""
Tests for API module.
"""

import pytest
from pygeospatial.api import config, gpu_backend, cpu_backend


class TestConfig:
    """Test configuration management."""
    
    def test_config_backend(self):
        """Test backend configuration."""
        assert config.backend == "cpu"  # Default
        
        # Try to set GPU backend (may fail if GPU not available)
        try:
            config.set_backend("gpu")
            # If successful, reset to CPU
            config.set_backend("cpu")
        except RuntimeError:
            # GPU not available, that's okay
            pass
        
        assert config.backend == "cpu"
    
    def test_config_invalid_backend(self):
        """Test invalid backend raises error."""
        with pytest.raises(ValueError):
            config.set_backend("invalid")
    
    def test_config_num_workers(self):
        """Test num workers configuration."""
        config.set_num_workers(4)
        assert config.num_workers == 4
        
        config.set_num_workers(None)
        assert config.num_workers is None
    
    def test_config_invalid_workers(self):
        """Test invalid workers raises error."""
        with pytest.raises(ValueError):
            config.set_num_workers(0)
    
    def test_config_cache_size(self):
        """Test cache size configuration."""
        config.set_cache_size("2GB")
        assert config.cache_size == "2GB"
    
    def test_config_log_level(self):
        """Test log level configuration."""
        config.set_log_level("DEBUG")
        assert config.log_level == "DEBUG"
        
        config.set_log_level("INFO")
        assert config.log_level == "INFO"
    
    def test_config_invalid_log_level(self):
        """Test invalid log level raises error."""
        with pytest.raises(ValueError):
            config.set_log_level("INVALID")
    
    def test_config_backend_info(self):
        """Test getting backend info."""
        info = config.get_backend_info()
        assert "cpu" in info
        assert "gpu" in info
        assert "current" in info


class TestContextManagers:
    """Test context managers for backend switching."""
    
    def test_cpu_backend_context(self):
        """Test CPU backend context manager."""
        config.set_backend("cpu")
        assert config.backend == "cpu"
        
        with cpu_backend():
            assert config.backend == "cpu"
        
        assert config.backend == "cpu"
    
    def test_gpu_backend_context(self):
        """Test GPU backend context manager."""
        config.set_backend("cpu")
        assert config.backend == "cpu"
        
        try:
            with gpu_backend():
                assert config.backend == "gpu"
            
            assert config.backend == "cpu"
        except RuntimeError:
            # GPU not available, skip this test
            pass
