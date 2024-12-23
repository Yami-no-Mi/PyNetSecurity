from server import app
import os
import subprocess
import time
from colorama import Fore, Style, init

# Initialize colorama for cross-platform support
init(autoreset=True)

def clear_screen():
    """Clear the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def check_python():
    """Check if Python is installed and return the version."""
    try:
        result = subprocess.run(["python", "--version"], check=True, capture_output=True, text=True)
        return f"{Fore.GREEN}[✓] Python is installed. Version: {result.stdout.strip()}"
    except FileNotFoundError:
        return f"{Fore.RED}[!] Python is not installed. Please install Python to proceed."
    except Exception as e:
        return f"{Fore.RED}[!] An error occurred: {str(e)}"

def run_tool():
    """Run the main tool by starting the Flask server."""
    try:
        print(Fore.GREEN + "[✓] Starting the tool... Server is running!")
        subprocess.run(["python", "backend/app.py"], check=True)
    except FileNotFoundError:
        print(Fore.RED + "[!] Error: app.py not found in the backend directory.")
    except Exception as e:
        print(Fore.RED + f"[!] Error while running the tool: {str(e)}")

def settings():
    """Display settings options and handle user input."""
    while True:
        clear_screen()
        print(Fore.CYAN + "\n=== Settings ===")
        time.sleep(0.2)
        print(Fore.YELLOW + " [1] Update API keys (Not implemented)")
        time.sleep(0.2)
        print(Fore.YELLOW + " [2] Change configuration (Not implemented)")
        time.sleep(0.2)
        print(Fore.YELLOW + " [3] Back to main menu")
        
        choice = input(Fore.RED + " ┌─[" + Fore.LIGHTGREEN_EX + "SETTINGS" + Fore.RED + "]\n └──╼ " + Fore.WHITE + "$ ").strip()
        
        if choice == "1":
            print(Fore.GREEN + "[*] Updating API keys... (Feature not implemented)")
            time.sleep(1)
        elif choice == "2":
            print(Fore.GREEN + "[*] Changing configuration... (Feature not implemented)")
            time.sleep(1)
        elif choice == "3":
            break
        else:
            print(Fore.RED + "[!] Invalid choice. Please try again.")
            time.sleep(1)

def main_menu():
    """Display the main menu and handle user input."""
    while True:
        clear_screen()
        print(Fore.CYAN + "\n=== IP Geolocation Finder ===")
        time.sleep(0.2)
        print(Fore.LIGHTYELLOW_EX + " [1] Run the tool")
        time.sleep(0.2)
        print(Fore.LIGHTYELLOW_EX + " [2] Check Python installation")
        time.sleep(0.2)
        print(Fore.LIGHTYELLOW_EX + " [3] Settings")
        time.sleep(0.2)
        print(Fore.LIGHTYELLOW_EX + " [4] Exit")
        
        choice = input(Fore.RED + " ┌─[" + Fore.LIGHTGREEN_EX + "MAIN MENU" + Fore.RED + "]\n └──╼ " + Fore.WHITE + "$ ").strip()

        if choice == "1":
            print(Fore.GREEN + "[*] Starting the tool...")
            time.sleep(1)
            app.start_server()
        elif choice == "2":
            print(check_python())  # Check Python installation
            input(Fore.YELLOW + "\nPress Enter to return to the menu.")
        elif choice == "3":
            settings()  # Show settings menu
        elif choice == "4":
            print(Fore.CYAN + "[*] Exiting the program. Goodbye!")
            break
        else:
            print(Fore.RED + "[!] Invalid choice. Please try again.")
            time.sleep(1)

if __name__ == "__main__":
    main_menu()