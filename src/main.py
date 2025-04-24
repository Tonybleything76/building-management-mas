import asyncio
import argparse
from datetime import datetime
from rich.console import Console
from rich.markdown import Markdown

from src.agents import initialize_agents, run_scenario
from src.scenarios import (
    create_normal_scenario,
    create_single_issue_scenario,
    create_multiple_issues_scenario
)
from src.building_data import BuildingData

console = Console()

async def run_cli_interface():
    """Run a simple command-line interface for the multi-agent system"""
    console.print(Markdown("# Building Management Multi-Agent System"))
    console.print("Initializing agents...")
    
    # Initialize the agents
    team, model_client = await initialize_agents()
    
    try:
        while True:
            console.print("\nSelect an option:")
            console.print("1. Run normal operations scenario")
            console.print("2. Run single issue scenario")
            console.print("3. Run multiple issues scenario (demo)")
            console.print("4. Input custom building data")
            console.print("5. Exit")
            
            choice = input("\nEnter your choice (1-5): ")
            
            if choice == "1":
                scenario = create_normal_scenario()
                console.print("\nRunning normal operations scenario...")
            elif choice == "2":
                scenario = create_single_issue_scenario()
                console.print("\nRunning single issue scenario...")
            elif choice == "3":
                scenario = create_multiple_issues_scenario()
                console.print("\nRunning multiple issues scenario (demo)...")
            elif choice == "4":
                console.print("\nEnter custom building data:")
                building_id = input("Building ID: ")
                
                hvac_data = {}
                console.print("\nEnter HVAC data (empty line to finish):")
                while True:
                    system = input("HVAC System Name (or empty to finish): ")
                    if not system:
                        break
                    status = input(f"Status for {system}: ")
                    hvac_data[system] = status
                
                equipment_data = {}
                console.print("\nEnter Equipment data (empty line to finish):")
                while True:
                    equipment = input("Equipment Name (or empty to finish): ")
                    if not equipment:
                        break
                    status = input(f"Status for {equipment}: ")
                    equipment_data[equipment] = status
                
                safety_data = {}
                console.print("\nEnter Safety data (empty line to finish):")
                while True:
                    system = input("Safety System Name (or empty to finish): ")
                    if not system:
                        break
                    status = input(f"Status for {system}: ")
                    safety_data[system] = status
                
                scenario = BuildingData(
                    hvac_data=hvac_data,
                    equipment_data=equipment_data,
                    safety_data=safety_data,
                    building_id=building_id
                )
                console.print("\nRunning custom scenario...")
            elif choice == "5":
                console.print("\nExiting...")
                break
            else:
                console.print("\nInvalid choice. Please try again.")
                continue
            
            # Run the selected scenario
            console.print(Markdown("## Processing Building Data"))
            console.print("This may take a minute or two...\n")
            
            result = await run_scenario(team, scenario)
            
            # Display the result
            console.print(Markdown("## Analysis Complete"))
            console.print(Markdown(result))
            
            # Option to save the result
            save_option = input("\nSave this analysis to file? (y/n): ")
            if save_option.lower() == 'y':
                filename = f"analysis_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
                with open(filename, 'w') as f:
                    f.write(f"# Building Management Analysis\n\n")
                    f.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
                    f.write(f"## Building Data\n\n```\n{scenario.to_prompt()}\n```\n\n")
                    f.write(f"## Analysis Result\n\n{result}")
                console.print(f"Analysis saved to {filename}")
    
    finally:
        # Close the model client
        await model_client.close()

async def run_headless(scenario_type="normal", output_file=None):
    """Run the system in headless mode with a specified scenario"""
    # Initialize the agents
    team, model_client = await initialize_agents()
    
    try:
        # Select scenario
        if scenario_type == "normal":
            scenario = create_normal_scenario()
        elif scenario_type == "single":
            scenario = create_single_issue_scenario()
        elif scenario_type == "multiple":
            scenario = create_multiple_issues_scenario()
        else:
            raise ValueError(f"Unknown scenario type: {scenario_type}")
        
        # Run the scenario
        result = await run_scenario(team, scenario)
        
        # Save or print the result
        if output_file:
            with open(output_file, 'w') as f:
                f.write(f"# Building Management Analysis\n\n")
                f.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
                f.write(f"## Building Data\n\n```\n{scenario.to_prompt()}\n```\n\n")
                f.write(f"## Analysis Result\n\n{result}")
            print(f"Analysis saved to {output_file}")
        else:
            print(result)
    
    finally:
        # Close the model client
        await model_client.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Building Management Multi-Agent System")
    parser.add_argument("--headless", action="store_true", help="Run in headless mode")
    parser.add_argument("--scenario", choices=["normal", "single", "multiple"], 
                        default="normal", help="Scenario type for headless mode")
    parser.add_argument("--output", type=str, help="Output file for headless mode")
    
    args = parser.parse_args()
    
    if args.headless:
        asyncio.run(run_headless(args.scenario, args.output))
    else:
        asyncio.run(run_cli_interface())

