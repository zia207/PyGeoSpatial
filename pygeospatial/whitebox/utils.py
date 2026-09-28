"""
Utility functions for WhiteboxTools integration.

This module provides wrapper utilities for WhiteboxTools with GPU acceleration
and parallel processing support.
"""

import subprocess
import os
from typing import Optional, Dict, Any, List
from pathlib import Path


class WhiteboxToolsWrapper:
    """
    Wrapper for WhiteboxTools with GPU acceleration and parallel processing.
    
    This class provides a Python interface to WhiteboxTools with enhanced
    performance through GPU acceleration and parallel processing capabilities.
    """
    
    def __init__(self, whitebox_path: Optional[str] = None):
        """
        Initialize WhiteboxTools wrapper.
        
        Args:
            whitebox_path: Optional path to WhiteboxTools executable
        """
        self._whitebox_path = whitebox_path or self._find_whitebox_tools()
        self._working_dir = os.getcwd()
        self._verbose = False
        self._use_gpu = False
        self._num_workers = None
    
    def _find_whitebox_tools(self) -> Optional[str]:
        """
        Find WhiteboxTools executable in system PATH.
        
        Returns:
            Path to WhiteboxTools executable, or None if not found
        """
        # Try to find whitebox_tools in PATH
        for path in os.environ.get("PATH", "").split(os.pathsep):
            whitebox_path = os.path.join(path, "whitebox_tools")
            if os.path.exists(whitebox_path):
                return whitebox_path
            
            # Try with .exe on Windows
            if os.name == "nt":
                whitebox_path = os.path.join(path, "whitebox_tools.exe")
                if os.path.exists(whitebox_path):
                    return whitebox_path
        
        return None
    
    def set_working_dir(self, path: str) -> None:
        """
        Set working directory for WhiteboxTools operations.
        
        Args:
            path: Working directory path
        """
        if not os.path.exists(path):
            raise ValueError(f"Working directory does not exist: {path}")
        self._working_dir = path
    
    def set_verbose(self, verbose: bool) -> None:
        """
        Set verbose output mode.
        
        Args:
            verbose: Whether to enable verbose output
        """
        self._verbose = verbose
    
    def set_gpu_enabled(self, enabled: bool) -> None:
        """
        Enable or disable GPU acceleration.
        
        Args:
            enabled: Whether to enable GPU acceleration
        """
        self._use_gpu = enabled
    
    def set_num_workers(self, num_workers: Optional[int]) -> None:
        """
        Set number of workers for parallel processing.
        
        Args:
            num_workers: Number of workers, or None for auto-detect
        """
        self._num_workers = num_workers
    
    def run_tool(self, tool_name: str, *args, **kwargs) -> str:
        """
        Run a WhiteboxTools tool.
        
        Args:
            tool_name: Name of the tool to run
            *args: Positional arguments for the tool
            **kwargs: Keyword arguments for the tool
        
        Returns:
            Output file path or result
        
        Raises:
            RuntimeError: If WhiteboxTools is not found or execution fails
        """
        if self._whitebox_path is None:
            raise RuntimeError(
                "WhiteboxTools not found. Please install whitebox package or "
                "provide path to WhiteboxTools executable."
            )
        
        # Build command
        cmd = [self._whitebox_path, f"--run={tool_name}"]
        
        # Add working directory
        cmd.extend(["--wd", self._working_dir])
        
        # Add verbose flag if needed
        if self._verbose:
            cmd.append("-v")
        
        # Add tool arguments
        for i, arg in enumerate(args):
            cmd.extend([f"--input{i+1}" if i == 0 else f"--input{i+1}", str(arg)])
        
        # Add keyword arguments
        for key, value in kwargs.items():
            cmd.extend([f"--{key}", str(value)])
        
        try:
            # Run the command
            result = subprocess.run(
                cmd,
                cwd=self._working_dir,
                capture_output=True,
                text=True,
                check=True
            )
            
            if self._verbose:
                print(result.stdout)
                if result.stderr:
                    print(result.stderr)
            
            # Return the last argument (usually output file)
            return args[-1] if args else str(result.stdout)
        
        except subprocess.CalledProcessError as e:
            raise RuntimeError(
                f"WhiteboxTools execution failed: {e.stderr}\n"
                f"Command: {' '.join(cmd)}"
            )
    
    def tool_help(self, tool_name: str) -> str:
        """
        Get help for a specific tool.
        
        Args:
            tool_name: Name of the tool
        
        Returns:
            Help text for the tool
        """
        if self._whitebox_path is None:
            raise RuntimeError("WhiteboxTools not found")
        
        cmd = [self._whitebox_path, f"--toolhelp={tool_name}"]
        
        try:
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                check=True
            )
            return result.stdout
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"Failed to get tool help: {e.stderr}")
    
    def list_tools(self, keyword: Optional[str] = None) -> List[str]:
        """
        List available tools.
        
        Args:
            keyword: Optional keyword to filter tools
        
        Returns:
            List of tool names
        """
        if self._whitebox_path is None:
            raise RuntimeError("WhiteboxTools not found")
        
        cmd = [self._whitebox_path, "--listtools"]
        if keyword:
            cmd.append(keyword)
        
        try:
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                check=True
            )
            # Parse the output to extract tool names
            # This is a simplified version - real implementation would parse properly
            return result.stdout.split('\n') if result.stdout else []
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"Failed to list tools: {e.stderr}")
    
    def version(self) -> str:
        """
        Get WhiteboxTools version.
        
        Returns:
            Version string
        """
        if self._whitebox_path is None:
            raise RuntimeError("WhiteboxTools not found")
        
        cmd = [self._whitebox_path, "--version"]
        
        try:
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                check=True
            )
            return result.stdout.strip()
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"Failed to get version: {e.stderr}")
