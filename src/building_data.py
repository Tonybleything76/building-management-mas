from dataclasses import dataclass, field
from typing import Dict, Optional
from datetime import datetime

@dataclass
class BuildingData:
    """Data structure for building information"""
    building_id: str
    timestamp: str = field(default_factory=lambda: datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    hvac_data: Dict[str, str] = field(default_factory=dict)
    equipment_data: Dict[str, str] = field(default_factory=dict)
    safety_data: Dict[str, str] = field(default_factory=dict)
    
    def to_dict(self) -> dict:
        """Convert building data to dictionary"""
        return {
            "building_id": self.building_id,
            "timestamp": self.timestamp,
            "hvac_data": self.hvac_data,
            "equipment_data": self.equipment_data,
            "safety_data": self.safety_data
        }
    
    def to_prompt(self) -> str:
        """Convert building data to a prompt for the agents"""
        prompt = f"Building ID: {self.building_id}\n"
        prompt += f"Timestamp: {self.timestamp}\n\n"
        
        prompt += "HVAC Systems:\n"
        for system, data in self.hvac_data.items():
            prompt += f"- {system}: {data}\n"
        
        prompt += "\nEquipment Status:\n"
        for equipment, data in self.equipment_data.items():
            prompt += f"- {equipment}: {data}\n"
        
        prompt += "\nSafety Systems:\n"
        for system, data in self.safety_data.items():
            prompt += f"- {system}: {data}\n"
        
        return prompt

