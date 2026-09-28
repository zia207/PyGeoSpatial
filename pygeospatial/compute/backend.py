"""
Compute backend abstraction for Py-GeoSpatial.

This module provides the backend abstraction for CPU and GPU computing,
allowing spatial operations to be executed on different compute devices.
"""

from abc import ABC, abstractmethod
from typing import Any, Optional, Dict, List
import multiprocessing
import os


class ComputeBackend(ABC):
    """
    Abstract base class for compute backends.
    
    This class defines the interface that all compute backends must implement,
    providing a unified interface for CPU and GPU operations.
    """
    
    def __init__(self):
        """Initialize compute backend."""
        self._device_info: Optional[Dict[str, Any]] = None
        self._available: bool = self._check_availability()
    
    @property
    def available(self) -> bool:
        """Check if backend is available."""
        return self._available
    
    @property
    def device_info(self) -> Dict[str, Any]:
        """Get device information."""
        if self._device_info is None:
            self._device_info = self._get_device_info()
        return self._device_info
    
    @abstractmethod
    def _check_availability(self) -> bool:
        """Check if backend is available."""
        pass
    
    @abstractmethod
    def _get_device_info(self) -> Dict[str, Any]:
        """Get device information."""
        pass
    
    @abstractmethod
    def execute(self, operation: str, *args, **kwargs) -> Any:
        """
        Execute an operation on this backend.
        
        Args:
            operation: Operation to execute
            *args: Positional arguments
            **kwargs: Keyword arguments
        
        Returns:
            Operation result
        """
        pass
    
    @abstractmethod
    def allocate_memory(self, size: int) -> Any:
        """
        Allocate memory on device.
        
        Args:
            size: Size in bytes
        
        Returns:
            Memory handle
        """
        pass
    
    @abstractmethod
    def free_memory(self, handle: Any) -> None:
        """
        Free allocated memory.
        
        Args:
            handle: Memory handle to free
        """
        pass
    
    @abstractmethod
    def transfer_to_device(self, data: Any) -> Any:
        """
        Transfer data to device.
        
        Args:
            data: Data to transfer
        
        Returns:
            Device data handle
        """
        pass
    
    @abstractmethod
    def transfer_from_device(self, handle: Any) -> Any:
        """
        Transfer data from device.
        
        Args:
            handle: Device data handle
        
        Returns:
            Host data
        """
        pass


class CPUBackend(ComputeBackend):
    """
    CPU-based compute backend.
    
    This backend provides CPU-based computing with multi-core support
    through multiprocessing.
    """
    
    def __init__(self, num_workers: Optional[int] = None):
        """
        Initialize CPU backend.
        
        Args:
            num_workers: Number of worker processes, or None for auto-detect
        """
        self._num_workers = num_workers or multiprocessing.cpu_count()
        super().__init__()
    
    def _check_availability(self) -> bool:
        """CPU backend is always available."""
        return True
    
    def _get_device_info(self) -> Dict[str, Any]:
        """Get CPU device information."""
        return {
            "type": "CPU",
            "num_cores": multiprocessing.cpu_count(),
            "num_workers": self._num_workers,
            "architecture": os.uname().machine if hasattr(os, 'uname') else "unknown"
        }
    
    def execute(self, operation: str, *args, **kwargs) -> Any:
        """
        Execute operation on CPU.
        
        For now, this is a placeholder. In the full implementation,
        this would dispatch to appropriate CPU-based algorithms.
        """
        # Placeholder - in full implementation, this would execute
        # the operation using CPU-based algorithms
        raise NotImplementedError(f"CPU execution not yet implemented for: {operation}")
    
    def allocate_memory(self, size: int) -> Any:
        """Allocate memory on CPU (returns size for tracking)."""
        # CPU memory allocation is handled by Python's memory manager
        # This is mainly for consistency with GPU backend interface
        return size
    
    def free_memory(self, handle: Any) -> None:
        """Free CPU memory (no-op for CPU backend)."""
        # CPU memory is managed by Python's garbage collector
        pass
    
    def transfer_to_device(self, data: Any) -> Any:
        """Transfer data to CPU (no-op, data already on CPU)."""
        return data
    
    def transfer_from_device(self, handle: Any) -> Any:
        """Transfer data from CPU (no-op, data already on CPU)."""
        return handle
    
    @property
    def num_workers(self) -> int:
        """Get number of worker processes."""
        return self._num_workers
    
    def set_num_workers(self, num_workers: int) -> None:
        """
        Set number of worker processes.
        
        Args:
            num_workers: Number of workers
        """
        if num_workers < 1:
            raise ValueError("num_workers must be >= 1")
        self._num_workers = num_workers
        self._device_info = None  # Invalidate cached info


class GPUBackend(ComputeBackend):
    """
    GPU-based compute backend.
    
    This backend provides GPU-based computing using CUDA or OpenCL.
    """
    
    def __init__(self, platform: str = "cuda"):
        """
        Initialize GPU backend.
        
        Args:
            platform: GPU platform ("cuda" or "opencl")
        """
        self._platform = platform
        self._cupy_available = False
        self._device_id = 0
        super().__init__()
    
    def _check_availability(self) -> bool:
        """Check if GPU backend is available."""
        try:
            if self._platform == "cuda":
                import cupy as cp
                self._cupy_available = True
                return True
            elif self._platform == "opencl":
                # OpenCL check would go here
                return False  # Not implemented yet
        except ImportError:
            return False
        return False
    
    def _get_device_info(self) -> Dict[str, Any]:
        """Get GPU device information."""
        if not self._available:
            return {"type": "GPU", "available": False}
        
        if self._platform == "cuda" and self._cupy_available:
            try:
                import cupy as cp
                device = cp.cuda.Device()
                mempool = cp.get_default_memory_pool()
                return {
                    "type": "GPU",
                    "platform": "CUDA",
                    "device_id": self._device_id,
                    "device_name": device.name,
                    "compute_capability": device.compute_capability,
                    "total_memory": device.mem_info[0],
                    "free_memory": device.mem_info[1],
                    "memory_used": mempool.used_bytes(),
                    "memory_limit": mempool.get_limit()
                }
            except Exception as e:
                return {"type": "GPU", "platform": "CUDA", "error": str(e)}
        
        return {"type": "GPU", "platform": self._platform, "available": False}
    
    def execute(self, operation: str, *args, **kwargs) -> Any:
        """
        Execute operation on GPU.
        
        For now, this is a placeholder. In the full implementation,
        this would dispatch to appropriate GPU-based algorithms.
        """
        if not self._available:
            raise RuntimeError("GPU backend is not available")
        
        # Placeholder - in full implementation, this would execute
        # the operation using GPU-based algorithms
        raise NotImplementedError(f"GPU execution not yet implemented for: {operation}")
    
    def allocate_memory(self, size: int) -> Any:
        """Allocate memory on GPU."""
        if not self._available:
            raise RuntimeError("GPU backend is not available")
        
        if self._platform == "cuda" and self._cupy_available:
            import cupy as cp
            return cp.cuda.memory.alloc(size)
        
        raise NotImplementedError(f"Memory allocation not implemented for {self._platform}")
    
    def free_memory(self, handle: Any) -> None:
        """Free GPU memory."""
        if not self._available:
            raise RuntimeError("GPU backend is not available")
        
        # GPU memory is managed by the framework (CuPy, etc.)
        # This is mainly for explicit cleanup if needed
        if hasattr(handle, 'free'):
            handle.free()
    
    def transfer_to_device(self, data: Any) -> Any:
        """Transfer data to GPU."""
        if not self._available:
            raise RuntimeError("GPU backend is not available")
        
        if self._platform == "cuda" and self._cupy_available:
            import cupy as cp
            import numpy as np
            if isinstance(data, np.ndarray):
                return cp.asarray(data)
            return data
        
        raise NotImplementedError(f"Data transfer not implemented for {self._platform}")
    
    def transfer_from_device(self, handle: Any) -> Any:
        """Transfer data from GPU."""
        if not self._available:
            raise RuntimeError("GPU backend is not available")
        
        if self._platform == "cuda" and self._cupy_available:
            import cupy as cp
            import numpy as np
            if isinstance(handle, cp.ndarray):
                return cp.asnumpy(handle)
            return handle
        
        raise NotImplementedError(f"Data transfer not implemented for {self._platform}")
    
    def set_device(self, device_id: int) -> None:
        """
        Set GPU device.
        
        Args:
            device_id: GPU device ID
        """
        if not self._available:
            raise RuntimeError("GPU backend is not available")
        
        if self._platform == "cuda" and self._cupy_available:
            import cupy as cp
            cp.cuda.Device(device_id).use()
            self._device_id = device_id
            self._device_info = None  # Invalidate cached info
        else:
            raise NotImplementedError(f"Device selection not implemented for {self._platform}")


class BackendManager:
    """
    Manager for compute backends.
    
    This class manages the available compute backends and provides
    a unified interface for backend selection and operations.
    """
    
    def __init__(self):
        """Initialize backend manager."""
        self._cpu_backend = CPUBackend()
        self._gpu_backend = None
        self._current_backend = self._cpu_backend
    
    @property
    def cpu_backend(self) -> CPUBackend:
        """Get CPU backend."""
        return self._cpu_backend
    
    @property
    def gpu_backend(self) -> Optional[GPUBackend]:
        """Get GPU backend."""
        return self._gpu_backend
    
    @property
    def current_backend(self) -> ComputeBackend:
        """Get current backend."""
        return self._current_backend
    
    def initialize_gpu(self, platform: str = "cuda") -> bool:
        """
        Initialize GPU backend.
        
        Args:
            platform: GPU platform ("cuda" or "opencl")
        
        Returns:
            True if GPU backend was successfully initialized
        """
        try:
            self._gpu_backend = GPUBackend(platform)
            if self._gpu_backend.available:
                return True
            self._gpu_backend = None
            return False
        except Exception:
            self._gpu_backend = None
            return False
    
    def set_backend(self, backend_type: str) -> None:
        """
        Set current backend.
        
        Args:
            backend_type: Either "cpu" or "gpu"
        """
        if backend_type == "cpu":
            self._current_backend = self._cpu_backend
        elif backend_type == "gpu":
            if self._gpu_backend is None or not self._gpu_backend.available:
                raise RuntimeError("GPU backend is not available")
            self._current_backend = self._gpu_backend
        else:
            raise ValueError(f"Invalid backend type: {backend_type}")
    
    def get_backend_info(self) -> Dict[str, Any]:
        """
        Get information about available backends.
        
        Returns:
            Dictionary with backend information
        """
        return {
            "cpu": {
                "available": self._cpu_backend.available,
                "info": self._cpu_backend.device_info
            },
            "gpu": {
                "available": self._gpu_backend.available if self._gpu_backend else False,
                "info": self._gpu_backend.device_info if self._gpu_backend else None
            },
            "current": str(type(self._current_backend).__name__)
        }


# Global backend manager instance
_backend_manager = BackendManager()


def get_backend_manager() -> BackendManager:
    """Get the global backend manager instance."""
    return _backend_manager
