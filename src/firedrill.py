import yaml
import os
from gpt import ask_gpt, init_chat_history, print_chat_history
from dotenv import load_dotenv

win_prompt = """
The incident has been resolved. Please now provide a post-incident performance summary for the user. Include:
A brief recap of how they resolved the incident.
An evaluation of their choices—what they did well, and what they could have done differently.

Praise for strong decisions around:
Investigation
Communication
Escalation
Mitigation
Overall approach

Adjust your tone and expectations based on the user’s apparent experience level.
If junior: be encouraging and educational
If senior: be direct and critical where appropriate
Provide a letter grade based on their performance.

Note:
If the user reached resolution via an alternative method not defined in the scenario, acknowledge their creativity and still issue a WIN message, followed by the same structured feedback.
Be clear, specific, and professional in tone.
"""

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
            print("🎉 You have successfully resolved the incident!  Please wait for your grade and feedback...")
            reply = ask_gpt(win_prompt)
            print("Feedback:")
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
