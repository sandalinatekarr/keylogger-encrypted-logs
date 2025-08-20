# Keylogger Encrypted Logs

## Overview
This Python project captures keyboard inputs, encrypts the logs, and uploads them to a server. It also provides functionality to decrypt the logs later. This project is intended for **educational purposes only**.

---

## ⚠️ Important Notice
**Ethical Use Only**: Unauthorized use of keyloggers is illegal. Only run this software on machines you own or have explicit permission to test on.

---

## Features
- Capture keystrokes in the background  
- Encrypt captured logs securely  
- Upload encrypted logs to a server  
- Decrypt logs for analysis  

---

## Project Structure
keylogger-encrypted-logs/
│
├── keylogger.py # Main keylogging script
├── encryptor.py # Handles encryption of logs
├── decryptor.py # Handles decryption of logs
├── upload_client.py # Uploads encrypted logs to server
├── server.py # Server to receive uploaded logs
├── requirements.txt # Python dependencies
└── .gitignore # Git ignore file


---

## Installation
1. Clone the repository:
```bash
git clone https://github.com/sandalinatekarr/keylogger-encrypted-logs.git
cd keylogger-encrypted-logs


Install dependencies:

pip install -r requirements.txt


Set up your server to receive uploaded logs (configure server.py as needed).

Usage

Start the server:

python server.py


Run the keylogger:

python keylogger.py


Decrypt logs:

python decryptor.py <encrypted_log_file>
