import requests
from colorama import Fore, Style, init
import os
import subprocess
import sys

# Initialize colorama for color support
init(autoreset=True)

def clear_screen():
    """Clear the console screen based on the operating system."""
    # If the OS is Windows, use 'cls'; for Unix-based systems, use 'clear'
    os.system('cls' if os.name == 'nt' else 'clear')

def get_ip_info(ip_address):
    """Fetch IP information from the ipinfo.io API."""
    # API endpoint for fetching IP information
    API_URL = f"https://ipinfo.io/{ip_address}?token=98eb2a223ae38d"
    try:
        # Make the GET request to the API
        response = requests.get(API_URL)
        if response.status_code == 200:
            # If the request is successful, return the JSON response
            return response.json()
        else:
            # If the request fails, return an error message with the status code
            return {"error": f"Unable to fetch data. Status code: {response.status_code}"}
    except Exception as e:
        # If there's any exception (e.g., network issues), return the error
        return {"error": str(e)}

def format_dict(data, level=1):
    """Recursively format nested dictionaries for better display."""
    output = ""
    for key, value in data.items():
        if isinstance(value, dict):
            # If the value is a dictionary, call format_dict recursively
            output += f"{Fore.GREEN}{'  ' * level}[*] {key}:{Style.RESET_ALL}\n"
            output += format_dict(value, level + 1)
        else:
            # For other types, print the key-value pair
            output += f"{Fore.CYAN}{'  ' * level}[*] {key}: {Fore.WHITE}{value}{Style.RESET_ALL}\n"
    return output

def print_ip_info(data):
    """Print IP information in a formatted and colored way."""
    # Print header
    print(Fore.YELLOW + "\n=== IP-Geolocation-Finder ===" + Style.RESET_ALL)

    # General IP information
    general_keys = {
        "ip": data.get("ip"),
        "hostname": data.get("hostname"),
        "city": data.get("city"),
        "region": data.get("region"),
        "country": data.get("country"),
        "loc": data.get("loc"),
        "postal": data.get("postal"),
        "timezone": data.get("timezone"),
        "anycast": data.get("anycast")
    }

    print(Fore.GREEN + "[*] GENERAL:" + Style.RESET_ALL)
    for key, value in general_keys.items():
        print(Fore.CYAN + f"  [*] {key}: {Fore.WHITE}{value}{Style.RESET_ALL}")

    # Detailed IP information
    detailed_keys = {
        "asn": data.get("asn"),
        "privacy": data.get("privacy")
    }

    for key, value in detailed_keys.items():
        if isinstance(value, dict):
            # If the value is a dictionary, print the nested data
            print(Fore.GREEN + f"[*] {key.upper()}:{Style.RESET_ALL}")
            print(format_dict(value))
        else:
            # For non-dictionary values, print them directly
            print(Fore.CYAN + f"[*] {key}: {Fore.WHITE}{value}{Style.RESET_ALL}")

    # Print footer
    print(Fore.YELLOW + "\n===========================\n" + Style.RESET_ALL)

def install_requirements():
    """Install required libraries from a 'requirements.txt' file."""
    try:
        # Try to install the necessary packages using pip
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print(Fore.GREEN + "Required libraries have been installed successfully." + Style.RESET_ALL)
    except subprocess.CalledProcessError:
        print(Fore.RED + "Failed to install required libraries. Please check 'requirements.txt'." + Style.RESET_ALL)

def main():
    """Main function to get IP information from user input."""
    # Check if necessary libraries are installed
    try:
        import requests
        import colorama
    except ImportError:
        # If libraries are not found, call the install_requirements function
        print(Fore.RED + "Required libraries are missing. Attempting to install..." + Style.RESET_ALL)
        install_requirements()
    
    # Clear the screen
    clear_screen()

    # Print welcome messages
    print(Fore.MAGENTA + "Welcome to the IP-Geolocation-Finder!" + Style.RESET_ALL)
    print(Fore.BLUE + "Enter an IP address to retrieve geolocation information." + Style.RESET_ALL)
    print(Fore.LIGHTBLACK_EX + "Type 'exit' to quit the application." + Style.RESET_ALL)

    while True:
        # Ask for user input (IP address)
        ip_address = input(Fore.CYAN + "\nEnter an IP address: " + Style.RESET_ALL).strip()
        
        # If the user wants to exit, break the loop
        if ip_address.lower() == 'exit':
            print(Fore.GREEN + "Exiting the tool. Goodbye!" + Style.RESET_ALL)
            break

        # If the user entered an IP address
        if ip_address:
            # Fetch IP information
            data = get_ip_info(ip_address)
            
            # If there was an error fetching the data, print the error
            if "error" in data:
                print(Fore.RED + f"Error: {data['error']}" + Style.RESET_ALL)
            else:
                # Print the IP information if successful
                print_ip_info(data)
        else:
            # Handle invalid input (empty string)
            print(Fore.RED + "Invalid input. Please enter a valid IP address." + Style.RESET_ALL)

# Check if the script is being executed directly
if __name__ == "__main__":
    main()
