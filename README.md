# Keylogger Encrypted Logs
*A Proof-of-Concept keylogger that encrypts logs and simulates exfiltration*

---

## ​ Project Overview
This is a Proof-of-Concept (PoC) encrypted keylogger built with Python. It captures user keystrokes, encrypts them (AES via Fernet), and simulates secure exfiltration of logs to a simple server.

> Built strictly for ethical testing and educational purposes.

---

## ​ Requirements
- `pynput` — capture keystrokes  
- `cryptography` — AES (Fernet) encryption  
- `Flask` — simple receiving server (or any HTTP handler)  
- `requests` — upload client for exfiltration  

All dependencies are listed in `requirements.txt`.

---

## ​ Folder Structure
```plaintext
keylogger-encrypted-logs/
├── keylogger.py        # Captures keystrokes -> log.txt
├── encryptor.py        # Encrypts log.txt -> log.enc (generates key.key)
├── decryptor.py        # (Optional) Decrypts encrypted logs using key.key
├── upload_client.py    # Sends log.enc to the server
├── server.py           # Flask server to receive encrypted logs
├── requirements.txt    # Python dependencies
└── .gitignore
✨ Features

✅ Captures keystrokes in real time

🔐 Encrypts logs with AES (Fernet symmetric key)

📤 Simulates log exfiltration to a Flask server

🔓 Decryptor included for recovery of logs

🛡️ Modular design: keylogger, encryption, upload, server, decryptor

⚙️ How It Works

Keylogging
keylogger.py records keystrokes and saves them into log.txt.

Encryption
encryptor.py generates a Fernet AES key (key.key) and encrypts log.txt into log.enc.

Server Setup
server.py runs a Flask server at http://localhost:5000/upload that accepts encrypted files.

Exfiltration
upload_client.py simulates sending log.enc to the server using an HTTP POST request.

Decryption
decryptor.py can be used with key.key to decrypt log.enc back into readable text.

🚀 Quick Start
git clone https://github.com/sandalinatekarr/keylogger-encrypted-logs.git
cd keylogger-encrypted-logs
pip install -r requirements.txt

🧭 Step-by-Step Usage
1) Start the Server
python server.py


Server will run at:

http://localhost:5000/upload

2) Run the Keylogger
python keylogger.py


Keystrokes → log.txt

Stop logging with ESC (or Ctrl+C)

3) Encrypt the Logs
python encryptor.py


Generates:

log.enc — encrypted log

key.key — secret key

4) Upload Encrypted Logs
python upload_client.py


Files saved on server under uploads/

5) Decrypt Logs (Optional)
python decryptor.py log.enc

🔮 Future Enhancements

🔄 Automatic key rotation for stronger encryption

🕵️ Stealth mode to run in the background without detection

⏱ Timestamps for keystrokes and integrity validation

📂 Centralized log management for multiple clients

🐳 Dockerized setup for easier deployment

✉️ Encrypted email/TLS log transfer instead of plain HTTP

📊 Visualization module to analyze decrypted logs
