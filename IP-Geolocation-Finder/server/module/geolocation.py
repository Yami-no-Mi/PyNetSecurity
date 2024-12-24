import requests

def get_ip_geolocation(ip):
    """Get geolocation data for a given IP address."""
    # API یا روش دیگری که برای دریافت اطلاعات موقعیت جغرافیایی استفاده می‌کنید
    try:
        response = requests.get(f"https://geolocation-db.com/json/{ip}&position=true")
        if response.status_code == 200:
            return response.json()
        else:
            return None
    except Exception as e:
        print(f"Error fetching geolocation: {str(e)}")
        return None
