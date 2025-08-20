# Keylogger Encrypted Logs
*A Proof-of-Concept keylogger that encrypts logs and simulates exfiltration*

---

## 📘 Project Overview
This is a Proof-of-Concept (PoC) encrypted keylogger built with Python. It captures user keystrokes, encrypts them (AES via Fernet), and simulates secure exfiltration of logs to a simple server.

> Built strictly for ethical testing and educational purposes.

---

## ✅ Requirements
- `pynput` — capture keystrokes  
- `cryptography` — AES (Fernet) encryption  
- `Flask` — simple receiving server (or any HTTP handler)  
- `requests` — upload client for exfiltration

All dependencies are listed in `requirements.txt`.

---

## 📁 Folder Structure
keylogger-encrypted-logs/
├─ keylogger.py # Captures keystrokes -> log.txt
├─ encryptor.py # Encrypts log.txt -> log.enc (generates key.key)
├─ decryptor.py # (Optional) Decrypts encrypted logs using key.key
├─ upload_client.py # Sends log.enc to the server
├─ server.py # Flask server to receive encrypted logs
├─ requirements.txt # Python dependencies
└─ .gitignore



