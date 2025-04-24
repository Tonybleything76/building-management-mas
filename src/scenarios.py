from src.building_data import BuildingData

def create_normal_scenario() -> BuildingData:
    """Create a scenario with normal operating conditions"""
    return BuildingData(
        building_id="Building-A",
        hvac_data={
            "Main HVAC": "Operating at 65% capacity, temperature setpoints maintained",
            "Zone 1 HVAC": "Operating at 60% capacity, normal operation",
            "Zone 2 HVAC": "Operating at 55% capacity, normal operation",
        },
        equipment_data={
            "Chiller #1": "Operating normally, no vibration anomalies",
            "Chiller #2": "Operating normally, no vibration anomalies",
            "Chiller #3": "In standby mode, scheduled maintenance completed last week",
        },
        safety_data={
            "CO2 Levels": "450 ppm average across all zones",
            "Emergency Lighting": "All systems operational",
            "Evacuation Routes": "All clear and accessible",
        }
    )

def create_single_issue_scenario() -> BuildingData:
    """Create a scenario with a single HVAC issue"""
    return BuildingData(
        building_id="Building-A",
        hvac_data={
            "Main HVAC": "Operating at 92% capacity, struggling to maintain temperature setpoints",
            "Zone 1 HVAC": "Operating at 60% capacity, normal operation",
            "Zone 2 HVAC": "Operating at 55% capacity, normal operation",
        },
        equipment_data={
            "Chiller #1": "Operating normally, no vibration anomalies",
            "Chiller #2": "Operating normally, no vibration anomalies",
            "Chiller #3": "In standby mode, scheduled maintenance completed last week",
        },
        safety_data={
            "CO2 Levels": "450 ppm average across all zones",
            "Emergency Lighting": "All systems operational",
            "Evacuation Routes": "All clear and accessible",
        }
    )

def create_multiple_issues_scenario() -> BuildingData:
    """Create a scenario with multiple simultaneous issues"""
    return BuildingData(
        building_id="Building-A",
        hvac_data={
            "Main HVAC": "Operating at 95% capacity, temperature setpoints not maintained",
            "Zone 1 HVAC": "Operating at 90% capacity, struggling with cold snap",
            "Zone 2 HVAC": "Operating at 85% capacity, struggling with cold snap",
        },
        equipment_data={
            "Chiller #1": "Operating at high load",
            "Chiller #2": "Operating at high load",
            "Chiller #3": "High vibration detected, potential mechanical issue",
        },
        safety_data={
            "CO2 Levels": "1200 ppm in atrium due to early arrival of 85 occupants",
            "Emergency Lighting": "Failure detected in key evacuation corridor",
            "Solar Panel Output": "Dropped to 25% under unexpected cloud cover",
        }
    )

