import unittest
from src.building_data import BuildingData

class TestBuildingData(unittest.TestCase):
    """Test cases for the BuildingData class"""
    
    def test_building_data_to_prompt(self):
        """Test conversion of building data to prompt"""
        data = BuildingData(
            hvac_data={"Main HVAC": "Test status"},
            equipment_data={"Chiller": "Test status"},
            safety_data={"CO2": "Test status"},
            building_id="Test-Building"
        )
        
        prompt = data.to_prompt()
        
        self.assertIn("Building ID: Test-Building", prompt)
        self.assertIn("Main HVAC: Test status", prompt)
        self.assertIn("Chiller: Test status", prompt)
        self.assertIn("CO2: Test status", prompt)
    
    def test_building_data_to_dict(self):
        """Test conversion of building data to dictionary"""
        data = BuildingData(
            hvac_data={"Main HVAC": "Test status"},
            equipment_data={"Chiller": "Test status"},
            safety_data={"CO2": "Test status"},
            building_id="Test-Building",
            timestamp="2025-04-24 08:00:00"
        )
        
        data_dict = data.to_dict()
        
        self.assertEqual(data_dict["building_id"], "Test-Building")
        self.assertEqual(data_dict["timestamp"], "2025-04-24 08:00:00")
        self.assertEqual(data_dict["hvac_data"], {"Main HVAC": "Test status"})
        self.assertEqual(data_dict["equipment_data"], {"Chiller": "Test status"})
        self.assertEqual(data_dict["safety_data"], {"CO2": "Test status"})

if __name__ == "__main__":
    unittest.main()
