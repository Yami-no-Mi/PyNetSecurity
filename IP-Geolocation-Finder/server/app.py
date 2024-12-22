from flask import Flask, send_from_directory
import os
import webbrowser
import threading

def start_server():
    """Start the Flask server and open the browser."""
    # مسیر اصلی پوشه IP-Geolocation-Finder
    base_path = os.path.join(os.getcwd(), "IP-Geolocation-Finder", "server")

    # پیکربندی Flask برای تنظیم پوشه استاتیک به دایرکتوری "server"
    app = Flask(__name__, static_folder=base_path)  # static_folder رو به پوشه server تنظیم می‌کنیم

    @app.route("/")
    def serve_index():
        """Serve the main HTML file (index.html)."""
        return send_from_directory(base_path, "index.html")  # فایل index.html رو از پوشه server می‌فرستیم

    @app.route("/static/<path:path>")
    def serve_static(path):
        """Serve static files like CSS and JavaScript."""
        return send_from_directory(os.path.join(base_path, "static"), path)  # فایل‌های استاتیک رو از پوشه static می‌فرستیم

    def open_browser():
        """Automatically open the default web browser."""
        webbrowser.open("http://127.0.0.1:5000/")

    # اجرای سرور در یک ترد جداگانه و باز کردن مرورگر در همان زمان
    threading.Thread(target=open_browser).start()

    # اجرای سرور Flask
    app.run(debug=True, use_reloader=False)

