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

## 📂 Folder Structure

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

### 1) Keylogging
`keylogger.py`  
Records keystrokes and saves them into `log.txt`.  
Stop logging with **ESC** (or `Ctrl+C`).  

---

### 2) Encryption
`encryptor.py`  
- Generates a secret key (`key.key`)  
- Encrypts `log.txt` → `log.enc`

---

### 3) Server Setup
`server.py`  
Runs a Flask server at:  http://localhost:5000/upload

Encrypted logs uploaded will be saved in the `uploads/` folder.  

---

### 4) Exfiltration Simulation
`upload_client.py`  
Uploads `log.enc` to the Flask server using an HTTP POST request.  

---

### 5) Decryption (Optional)
`decryptor.py`  
Decrypts `log.enc` using `key.key` back into readable text.  

---

## 🚀 Quick Start

### 1. Clone the repository
git clone https://github.com/sandalinatekarr/keylogger-encrypted-logs.git
cd keylogger-encrypted-logs

### 2. Install dependencies
pip install -r requirements.txt

### 3. Start the Flask server
python server.py

Server will run at:  
http://localhost:5000/upload

### 4. Run the keylogger
python keylogger.py

- Keystrokes will be saved to `log.txt`  
- Stop logging with **ESC** or `Ctrl+C`

### 5. Encrypt the logs
python encryptor.py

This will generate:  
- `log.enc` → Encrypted log file  
- `key.key` → Secret symmetric key  

### 6. Upload encrypted logs to server
python upload_client.py

Encrypted files will be saved in the server’s `uploads/` directory.  

### 7. (Optional) Decrypt logs
python decryptor.py log.enc

Decrypted output will be printed in the terminal or written to a file (based on your configuration).  

---

## 🔮 Future Enhancements
- 🔄 Automatic key rotation for stronger encryption  
- 🕵️ Stealth/background execution (simulation only)  
- ⏱ Timestamped keystrokes & integrity validation  
- 📂 Centralized log management for multiple clients  
- 🐳 Dockerized setup for quick deployment  
- ✉️ TLS/Email-based secure transfer of encrypted logs  
- 📊 Visualization of decrypted logs  

---

💡 **Educational Note**: This PoC is intended to help learners understand how encryption, secure data handling, and modular system design work together in practice.  

---
👉 This Markdown is ready to paste into your README.md — it will render clean, structured, and professional on GitHub.


