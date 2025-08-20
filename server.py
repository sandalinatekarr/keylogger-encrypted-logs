from flask import Flask, request
import os
import datetime

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Home route to avoid 404 on browser visit
@app.route("/")
def home():
    return "Server is running! Use /upload to POST encrypted logs."

@app.route("/upload", methods=["POST"])
def upload_file():
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    save_path = os.path.join(UPLOAD_FOLDER, f"log_{timestamp}.enc")

    # Get the raw request body safely
    data = request.get_data()
    print(f"[DEBUG] Received {len(data)} bytes")

    if not data:
        return "[!] No data received", 400

    # Write to file
    with open(save_path, "wb") as f:
        f.write(data)

    print(f"[+] Saved encrypted log to {save_path}")
    return "Upload successful", 200

if __name__ == "__main__":
    print("[*] Starting server at http://127.0.0.1:8000")
    app.run(host="0.0.0.0", port=8000)
