import requests
from colorama import Fore, Style, init
import os

# Initialize colorama for color support
init(autoreset=True)

def clear_screen():
    """Clear the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def get_ip_info(ip_address):
    """Fetch IP information from the ipinfo.io API."""
    API_URL = f"https://ipinfo.io/{ip_address}?token=98eb2a223ae38d"
    try:
        response = requests.get(API_URL)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Unable to fetch data. Status code: {response.status_code}"}
    except Exception as e:
        return {"error": str(e)}

def format_dict(data, level=1):
    """Format nested dictionaries for better display."""
    output = ""
    for key, value in data.items():
        if isinstance(value, dict):
            output += f"{Fore.GREEN}{'  ' * level}[*] {key}:{Style.RESET_ALL}\n"
            output += format_dict(value, level + 1)
        else:
            output += f"{Fore.CYAN}{'  ' * level}[*] {key}: {Fore.WHITE}{value}{Style.RESET_ALL}\n"
    return output

def print_ip_info(data):
    """Print IP information in a formatted and colored way."""
    print(Fore.YELLOW + "\n=== IP-Geolocation-Finder ===" + Style.RESET_ALL)

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

    detailed_keys = {
        "asn": data.get("asn"),
        "privacy": data.get("privacy")
    }

    for key, value in detailed_keys.items():
        if isinstance(value, dict):
            print(Fore.GREEN + f"[*] {key.upper()}:{Style.RESET_ALL}")
            print(format_dict(value))
        else:
            print(Fore.CYAN + f"[*] {key}: {Fore.WHITE}{value}{Style.RESET_ALL}")

    print(Fore.YELLOW + "\n===========================\n" + Style.RESET_ALL)

def main():
    """Main function to get IP information from user input."""
    clear_screen()
    print(Fore.MAGENTA + "Welcome to the IP-Geolocation-Finder!" + Style.RESET_ALL)
    print(Fore.BLUE + "Enter an IP address to retrieve geolocation information." + Style.RESET_ALL)
    print(Fore.LIGHTBLACK_EX + "Type 'exit' to quit the application." + Style.RESET_ALL)

    while True:
        ip_address = input(Fore.CYAN + "\nEnter an IP address: " + Style.RESET_ALL).strip()
        if ip_address.lower() == 'exit':
            print(Fore.GREEN + "Exiting the tool. Goodbye!" + Style.RESET_ALL)
            break

        if ip_address:
            data = get_ip_info(ip_address)
            if "error" in data:
                print(Fore.RED + f"Error: {data['error']}" + Style.RESET_ALL)
            else:
                print_ip_info(data)
        else:
            print(Fore.RED + "Invalid input. Please enter a valid IP address." + Style.RESET_ALL)

if __name__ == "__main__":
    main()