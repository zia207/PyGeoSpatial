"""
Tests for compute module.
"""

import pytest
from pygeospatial.compute import CPUBackend, GPUBackend, BackendManager, get_backend_manager


class TestCPUBackend:
    """Test CPU backend functionality."""
    
    def test_cpu_backend_creation(self):
        """Test creating CPU backend."""
        backend = CPUBackend()
        assert backend.available
        assert backend.num_workers > 0
    
    def test_cpu_backend_device_info(self):
        """Test CPU backend device info."""
        backend = CPUBackend()
        info = backend.device_info
        assert info["type"] == "CPU"
        assert "num_cores" in info
        assert "num_workers" in info
    
    def test_cpu_backend_num_workers(self):
        """Test setting number of workers."""
        backend = CPUBackend()
        backend.set_num_workers(4)
        assert backend.num_workers == 4
    
    def test_cpu_backend_invalid_workers(self):
        """Test invalid number of workers raises error."""
        backend = CPUBackend()
        with pytest.raises(ValueError):
            backend.set_num_workers(0)
    
    def test_cpu_backend_memory_operations(self):
        """Test CPU memory operations."""
        backend = CPUBackend()
        size = 1024
        handle = backend.allocate_memory(size)
        assert handle == size
        backend.free_memory(handle)
    
    def test_cpu_backend_data_transfer(self):
        """Test CPU data transfer (should be no-op)."""
        backend = CPUBackend()
        data = [1, 2, 3, 4, 5]
        device_data = backend.transfer_to_device(data)
        assert device_data is data
        
        host_data = backend.transfer_from_device(device_data)
        assert host_data is data


class TestGPUBackend:
    """Test GPU backend functionality."""
    
    def test_gpu_backend_creation(self):
        """Test creating GPU backend."""
        backend = GPUBackend()
        # GPU backend may not be available
        assert isinstance(backend.available, bool)
    
    def test_gpu_backend_device_info(self):
        """Test GPU backend device info."""
        backend = GPUBackend()
        info = backend.device_info
        assert info["type"] == "GPU"
    
    def test_gpu_backend_unavailable_operations(self):
        """Test operations fail when GPU unavailable."""
        backend = GPUBackend()
        if not backend.available:
            with pytest.raises(RuntimeError):
                backend.allocate_memory(1024)
            
            with pytest.raises(RuntimeError):
                backend.transfer_to_device([1, 2, 3])


class TestBackendManager:
    """Test backend manager functionality."""
    
    def test_backend_manager_creation(self):
        """Test creating backend manager."""
        manager = BackendManager()
        assert manager.cpu_backend.available
        assert manager.current_backend == manager.cpu_backend
    
    def test_backend_manager_set_cpu(self):
        """Test setting CPU backend."""
        manager = BackendManager()
        manager.set_backend("cpu")
        assert manager.current_backend == manager.cpu_backend
    
    def test_backend_manager_set_gpu_unavailable(self):
        """Test setting GPU backend when unavailable."""
        manager = BackendManager()
        if not manager.initialize_gpu():
            with pytest.raises(RuntimeError):
                manager.set_backend("gpu")
    
    def test_backend_manager_invalid_backend(self):
        """Test setting invalid backend type."""
        manager = BackendManager()
        with pytest.raises(ValueError):
            manager.set_backend("invalid")
    
    def test_backend_manager_info(self):
        """Test getting backend manager info."""
        manager = BackendManager()
        info = manager.get_backend_info()
        assert "cpu" in info
        assert "gpu" in info
        assert "current" in info
    
    def test_global_backend_manager(self):
        """Test global backend manager instance."""
        manager1 = get_backend_manager()
        manager2 = get_backend_manager()
        assert manager1 is manager2
