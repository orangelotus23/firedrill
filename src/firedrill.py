import yaml
import os
from gpt import ask_gpt, init_chat_history, print_chat_history
from dotenv import load_dotenv

def run_drill(scenario_path):
    with open(scenario_path, 'r') as f:
        scenario = yaml.safe_load(f)

    print()
    print(f"🔥 {scenario['title']}")
    print(f"ALERT: {scenario['description']}")
    print()

    # Initialize chat history with the scenario prompt
    init_chat_history(scenario)

    while True:
        user = input(">> What would you like to do next? (free text or hint or exit)...\n")
        if user.lower() in ["exit", "quit"]:
            print("Ending simulation.")
            break
        #print_chat_history()
        reply = ask_gpt(user)
        if "WIN" in reply:
            print()
            print("🎉 You have successfully resolved the incident!")
            print(reply)
            break
        print()
        print(reply)

    print("Resolution:")
    print(scenario['resolution'])

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python firedrill.py <scenario.yaml>")
    else:
        run_drill(sys.argv[1])
