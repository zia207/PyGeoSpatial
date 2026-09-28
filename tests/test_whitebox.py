"""
Tests for WhiteboxTools integration.
"""

import pytest
from pygeospatial.whitebox import WhiteboxToolsWrapper, get_whitebox_tools


class TestWhiteboxToolsWrapper:
    """Test WhiteboxTools wrapper functionality."""
    
    def test_wrapper_creation(self):
        """Test creating WhiteboxTools wrapper."""
        wrapper = WhiteboxToolsWrapper()
        assert wrapper is not None
    
    def test_working_dir_setting(self):
        """Test setting working directory."""
        import os
        wrapper = WhiteboxToolsWrapper()
        wrapper.set_working_dir(os.getcwd())
        assert wrapper._working_dir == os.getcwd()
    
    def test_working_dir_invalid(self):
        """Test invalid working directory raises error."""
        wrapper = WhiteboxToolsWrapper()
        with pytest.raises(ValueError):
            wrapper.set_working_dir("/nonexistent/path")
    
    def test_verbose_setting(self):
        """Test verbose setting."""
        wrapper = WhiteboxToolsWrapper()
        wrapper.set_verbose(True)
        assert wrapper._verbose is True
        
        wrapper.set_verbose(False)
        assert wrapper._verbose is False
    
    def test_gpu_setting(self):
        """Test GPU setting."""
        wrapper = WhiteboxToolsWrapper()
        wrapper.set_gpu_enabled(True)
        assert wrapper._use_gpu is True
        
        wrapper.set_gpu_enabled(False)
        assert wrapper._use_gpu is False
    
    def test_num_workers_setting(self):
        """Test num workers setting."""
        wrapper = WhiteboxToolsWrapper()
        wrapper.set_num_workers(4)
        assert wrapper._num_workers == 4
        
        wrapper.set_num_workers(None)
        assert wrapper._num_workers is None


class TestGlobalWhiteboxInstance:
    """Test global WhiteboxTools instance."""
    
    def test_get_whitebox_tools(self):
        """Test getting global WhiteboxTools instance."""
        wrapper = get_whitebox_tools()
        assert wrapper is not None
        
        # Should return same instance
        wrapper2 = get_whitebox_tools()
        assert wrapper is wrapper2
