from flask import Flask, send_from_directory
import os
import webbrowser
import threading
import sys

# Adding the server folder path to sys.path
sys.path.append(os.path.join(os.getcwd(), "IP-Geolocation-Finder", "server"))

from module import utils, geolocation


def start_server():
    """Start the Flask server and open the browser."""
    # The base path of the IP-Geolocation-Finder folder
    base_path = os.path.join(os.getcwd(), "IP-Geolocation-Finder", "server")

    # Configuring Flask to use the "server" directory for static files
    app = Flask(__name__, static_folder=base_path)

    @app.route("/")
    def serve_index():
        """Serve the main HTML file (index.html)."""
        utils.log_request("Serving index page.")  # Send a message to the log_request function
        return send_from_directory(base_path, "index.html")

    @app.route("/static/<path:path>")
    def serve_static(path):
        """Serve static files like CSS and JavaScript."""
        utils.log_request(f"Serving static file: {path}")  # Send a message to the log_request function
        return send_from_directory(os.path.join(base_path, "static"), path)

    def open_browser():
        """Automatically open the default web browser."""
        webbrowser.open("http://127.0.0.1:5000/")

    threading.Thread(target=open_browser).start()

    app.run(debug=True, use_reloader=False)
