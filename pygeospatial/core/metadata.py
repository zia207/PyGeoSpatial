"""
Metadata management for spatial datasets.

This module provides functionality for managing metadata associated with
geospatial datasets, including provenance, quality indicators, and custom
attributes.
"""

from typing import Dict, Any, Optional, List
from datetime import datetime
import json


class Metadata:
    """
    Metadata container for spatial datasets.
    
    This class stores and manages metadata information about spatial datasets,
    including creation time, data quality, processing history, and custom
    attributes.
    """
    
    def __init__(self):
        """Initialize empty metadata."""
        self._data: Dict[str, Any] = {
            "created": datetime.now().isoformat(),
            "modified": datetime.now().isoformat(),
            "attributes": {},
            "quality": {},
            "provenance": [],
        }
    
    @property
    def created(self) -> str:
        """Creation timestamp."""
        return self._data["created"]
    
    @property
    def modified(self) -> str:
        """Last modified timestamp."""
        return self._data["modified"]
    
    def update_modified(self) -> None:
        """Update modified timestamp to current time."""
        self._data["modified"] = datetime.now().isoformat()
    
    def set_attribute(self, key: str, value: Any) -> None:
        """
        Set a custom attribute.
        
        Args:
            key: Attribute key
            value: Attribute value
        """
        self._data["attributes"][key] = value
        self.update_modified()
    
    def get_attribute(self, key: str, default: Any = None) -> Any:
        """
        Get a custom attribute.
        
        Args:
            key: Attribute key
            default: Default value if key not found
        
        Returns:
            Attribute value or default
        """
        return self._data["attributes"].get(key, default)
    
    def remove_attribute(self, key: str) -> None:
        """
        Remove a custom attribute.
        
        Args:
            key: Attribute key to remove
        """
        if key in self._data["attributes"]:
            del self._data["attributes"][key]
            self.update_modified()
    
    @property
    def attributes(self) -> Dict[str, Any]:
        """Get all custom attributes."""
        return self._data["attributes"].copy()
    
    def set_quality_indicator(self, name: str, value: Any) -> None:
        """
        Set a data quality indicator.
        
        Args:
            name: Quality indicator name
            value: Quality indicator value
        """
        self._data["quality"][name] = value
        self.update_modified()
    
    def get_quality_indicator(self, name: str, default: Any = None) -> Any:
        """
        Get a data quality indicator.
        
        Args:
            name: Quality indicator name
            default: Default value if not found
        
        Returns:
            Quality indicator value or default
        """
        return self._data["quality"].get(name, default)
    
    @property
    def quality(self) -> Dict[str, Any]:
        """Get all quality indicators."""
        return self._data["quality"].copy()
    
    def add_provenance_entry(self, operation: str, parameters: Optional[Dict] = None) -> None:
        """
        Add a provenance entry (processing history).
        
        Args:
            operation: Operation performed
            parameters: Optional parameters used in operation
        """
        entry = {
            "operation": operation,
            "timestamp": datetime.now().isoformat(),
        }
        if parameters:
            entry["parameters"] = parameters
        
        self._data["provenance"].append(entry)
        self.update_modified()
    
    @property
    def provenance(self) -> List[Dict[str, Any]]:
        """Get processing history."""
        return self._data["provenance"].copy()
    
    def to_dict(self) -> Dict[str, Any]:
        """
        Convert metadata to dictionary.
        
        Returns:
            Dictionary representation of metadata
        """
        return self._data.copy()
    
    def to_json(self) -> str:
        """
        Convert metadata to JSON string.
        
        Returns:
            JSON string representation
        """
        return json.dumps(self._data, indent=2, default=str)
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Metadata":
        """
        Create metadata from dictionary.
        
        Args:
            data: Dictionary containing metadata
        
        Returns:
            Metadata object
        """
        metadata = cls()
        metadata._data = data.copy()
        return metadata
    
    @classmethod
    def from_json(cls, json_string: str) -> "Metadata":
        """
        Create metadata from JSON string.
        
        Args:
            json_string: JSON string containing metadata
        
        Returns:
            Metadata object
        """
        data = json.loads(json_string)
        return cls.from_dict(data)
    
    def __str__(self) -> str:
        """String representation."""
        return f"Metadata(attributes={len(self._data['attributes'])}, quality={len(self._data['quality'])})"
    
    def __repr__(self) -> str:
        """Detailed string representation."""
        return f"Metadata({self._data})"
