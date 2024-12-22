from server import app
import os
import subprocess

def check_python():
    """Check if Python is installed and return the version."""
    try:
        result = subprocess.run(["python", "--version"], check=True, capture_output=True, text=True)
        return f"Python is installed. Version: {result.stdout.strip()}"
    except FileNotFoundError:
        return "Python is not installed. Please install Python to proceed."
    except Exception as e:
        return f"An error occurred: {str(e)}"

def run_tool():
    """Run the main tool by starting the Flask server."""
    try:
        print("Starting the tool... Server is running!")
        subprocess.run(["python", "backend/app.py"], check=True)
    except FileNotFoundError:
        print("Error: app.py not found in the backend directory.")
    except Exception as e:
        print(f"Error while running the tool: {str(e)}")

def settings():
    """Display settings options and handle user input."""
    while True:
        print("\n=== Settings ===")
        print("1. Update API keys (Not implemented)")
        print("2. Change configuration (Not implemented)")
        print("3. Back to main menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            print("Updating API keys... (Feature not implemented)")
        elif choice == "2":
            print("Changing configuration... (Feature not implemented)")
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

def main_menu():
    """Display the main menu and handle user input."""
    while True:
        print("\n=== IP Geolocation Finder ===")
        print("1. Run the tool")
        print("2. Check Python installation")
        print("3. Settings")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            app.start_server()
        elif choice == "2":
            print(check_python())  # Check Python installation
        elif choice == "3":
            settings()  # Show settings menu
        elif choice == "4":
            print("Exiting the program. Goodbye!")  # Exit the program
            break
        else:
            print("Invalid choice. Please try again.")  # Invalid input handling

if __name__ == "__main__":
    main_menu()  # Start the program by calling main menu
