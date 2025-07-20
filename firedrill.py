import openai
import yaml
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def run_drill(scenario_path):
    with open(scenario_path, 'r') as f:
        scenario = yaml.safe_load(f)

    print(f"🔥 {scenario['title']}")
    print(scenario['description'])
    print()

    for step in scenario['timeline']:
        input(">> Press Enter to continue...")
        print(f"
📣 {step['message']}")
        print(f"💡 Hint: {step['hint']}")
        print()

    print("✅ Resolution:")
    print(scenario['resolution'])

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python firedrill.py <scenario.yaml>")
    else:
        run_drill(sys.argv[1])