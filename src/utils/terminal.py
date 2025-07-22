from colorama import Fore, Style, init
import re

init(autoreset=True)  # So colors reset automatically

def print_success(message):
    print(f"{Fore.GREEN}✅ {message}{Style.RESET_ALL}")

def print_warning(message):
    print(f"{Fore.YELLOW}⚠️ {message}{Style.RESET_ALL}")

def print_error(message):
    print(f"{Fore.RED}❌ {message}{Style.RESET_ALL}")

def print_hint(message):
    print(f"{Fore.CYAN}💡 {message}{Style.RESET_ALL}")

def print_user_input(message):
    print(f"{Fore.MAGENTA}🧠 {message}{Style.RESET_ALL}")

def print_timestamped(role, message):
    from datetime import datetime
    now = datetime.now().strftime("%H:%M")
    if role == "GPT":
        message = clean_bold_headings(message)
        print(f"{Fore.BLUE}🕒 [{now}] GPT: {message}{Style.RESET_ALL}")
    else:
        print(f"{Fore.MAGENTA}🕒 [{now}] You: {message}{Style.RESET_ALL}")

def clean_bold_headings(text):
    # Convert markdown-style bold and italic to plain
    text = re.sub(r"\*\*(.*?)\*\*", r"\1", text)
    text = re.sub(r"\*(.*?)\*", r"\1", text)
    return text

def print_separator(char="─", length=50):
    print("\n" + char * length + "\n")
