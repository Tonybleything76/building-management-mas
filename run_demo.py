import asyncio
from src.agents import initialize_agents, run_scenario
from src.scenarios import create_multiple_issues_scenario
from datetime import datetime

async def run_demo():
    print("=== Building Management Multi-Agent System Demo ===")
    print("Initializing agents...")
    
    # Initialize the agents
    team, model_client = await initialize_agents()
    
    try:
        # Create the multiple issues scenario
        scenario = create_multiple_issues_scenario()
        
        print("\nScenario: Multiple Issues")
        print("-------------------------")
        print(scenario.to_prompt())
        print("\nProcessing building data...")
        
        # Run the scenario
        result = await run_scenario(team, scenario)
        
        # Display the result
        print("\n=== Analysis Complete ===")
        print(result)
        
        # Save the result
        filename = f"demo_analysis_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
        with open(filename, 'w') as f:
            f.write(f"# Building Management Analysis\n\n")
            f.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            f.write(f"## Building Data\n\n```\n{scenario.to_prompt()}\n```\n\n")
            f.write(f"## Analysis Result\n\n{result}")
        print(f"\nAnalysis saved to {filename}")
    
    finally:
        # Close the model client
        await model_client.close()

if __name__ == "__main__":
    asyncio.run(run_demo())
