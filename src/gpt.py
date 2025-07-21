# gpt.py

import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set up client
base_url = os.getenv("BASE_URL")
key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=key) if not os.getenv("BASE_URL") else OpenAI(base_url=base_url, api_key="")

# Set your model (default to gpt-4o)
model = os.getenv("OPENAI_MODEL", "gpt-4o")

def init_chat_history(scenario_prompt):
    global chat_history
    chat_history = [
      {
        "role": "system",
        "content": f"""
      You are simulating an on-call incident for training purposes. The following scenario contains the ONLY valid facts about the incident:
      
      --- BEGIN SCENARIO ---
      {scenario_prompt}
      --- END SCENARIO ---
      
      RULES:
      1. You must NOT invent any facts or timeline events not included above.
      2. If the user asks about something that is not present in the scenario, say: "That detail isn't available right now. Try focusing on what we know so far."
      3. Only reveal timeline events when the user gives a plausible, relevant action that would uncover it (e.g., checking logs, calling someone, examining metrics).
      4. Stay in character as a training coach or simulation runner, guiding the user one step at a time.
      5. Never say 'I'm an AI language model.' Stay fully in character.
      6. Your job is to test the user's response to this simulated page and gradually reveal the scenario as they engage with it. Stay strict, stay consistent, and never make anything up.
      7. If the user seems to be way off track, you may gently redirect them to focus on the existing clues.
      8. If the user asks for a hint or help, you can provide a nudge in the right direction or another timeline detail without giving away the solution.
      9. When EITHER the user provides any of the keywords in scenario win_conditions OR you are otherwise satisfied that the user has resolved the issue, you must respond with the token "WIN" in your message and feedback for the user on their approach to the incident.
      10. In the WIN message, provide a brief summary of how the user resolved the incident and how they could have approached it differently.
      11. If the trainee provides a valid alternative solution that is not defined, you can trigger a WIN response as well, but you must still provide feedback on their approach.
      12. In your feedback summary, you should praise the trainee for not only their resolution to the incident but also their communications, their escalations, their mitigations, and their overall approach to the incident.
      13. Engage at the level the user is at. If they are a junior engineer, you can provide more hints and guidance. If they are a senior engineer, you can be more strict and expect them to drive the investigation. Give them a letter grade based on their level-adjusted performance.
      14. You are simulating a real-world on-call incident for training. The trainee is responding to alerts and investigating the issue.
      15. You have access to the full timeline of events and metadata, but you must only reveal timeline entries as the user makes investigative progress. If they ask good questions (e.g., about cache behavior or recent changes), show them timeline events that reflect their direction. If they stall, offer gentle hints.
      16. If the user asks for help from a teammate or another team (e.g. "ask the database team"), you can simulate a response from a teammate by providing a helpful hint or suggestion based on the scenario.
      17. Remind user of stakes: If the user starts to rabbit-hole or lose the plot, gently remind them of the impact, downtime, or urgency of the incident.
      18. Merciful WIN: If the user thinks they’re done but clearly missed something, you may end the scenario, declare a WIN, and dock their grade with explanation.
      19. Auto-hint on stall: If the user appears stuck or is floundering without progress, proactively offer a helpful hint even if they haven’t asked.
      """
      }
    ]

def print_chat_history():
    print("\n===== Chat History So Far =====")
    for message in chat_history:
        print(f"{message['role']}: {message['content']}")
    print("==============================\n")


def ask_gpt(user_input: str, temperature: float = 0.3) -> str:
    # Append user input to the chat history
    chat_history.append({"role": "user", "content": user_input})

    try:
        response = client.chat.completions.create(
            model=model,
            messages=chat_history,
            temperature=temperature
        )
        reply = response.choices[0].message.content

        # Append assistant reply to chat history
        chat_history.append({"role": "assistant", "content": reply})

        return reply

    except Exception as e:
        return f"Error talking to GPT: {e}"
