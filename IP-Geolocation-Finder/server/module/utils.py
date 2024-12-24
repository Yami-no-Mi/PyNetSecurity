import os

def log_request(message):
    """Log a request to the console."""
    print(f"[LOG] {message}")

def get_static_file_path(base_path, file_name):
    """Return the full path of a static file."""
    static_folder = os.path.join(base_path, "static")
    return os.path.join(static_folder, file_name)
