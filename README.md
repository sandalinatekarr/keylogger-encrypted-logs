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
```plaintext
keylogger-encrypted-logs/
├── keylogger.py        # Captures keystrokes -> log.txt
├── encryptor.py        # Encrypts log.txt -> log.enc (generates key.key)
├── decryptor.py        # (Optional) Decrypts encrypted logs using key.key
├── upload_client.py    # Sends log.enc to the server
├── server.py           # Flask server to receive encrypted logs
├── requirements.txt    # Python dependencies
└── .gitignore

---

## ⚙️ How It Works
1. **Keylogging**  
   `keylogger.py` records keystrokes and saves them into `log.txt`.

2. **Encryption**  
   `encryptor.py` generates a Fernet AES key (`key.key`) and encrypts `log.txt` into `log.enc`.

3. **Server Setup**  
   `server.py` runs a Flask server at `http://localhost:5000/upload` that accepts encrypted files.

4. **Exfiltration**  
   `upload_client.py` simulates sending `log.enc` to the server using an HTTP POST request.

5. **Decryption**  
   `decryptor.py` can be used with `key.key` to decrypt `log.enc` back into readable text.

---

## 🚀 Quick Start
```bash
git clone https://github.com/sandalinatekarr/keylogger-encrypted-logs.git
cd keylogger-encrypted-logs
pip install -r requirements.txt

