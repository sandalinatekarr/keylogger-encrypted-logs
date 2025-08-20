import os

UPLOADS_DIR = "uploads"

for filename in os.listdir(UPLOADS_DIR):
    path = os.path.join(UPLOADS_DIR, filename)
    if filename.endswith(".enc") and os.path.getsize(path) == 0:
        print(f"[x] Removing empty file: {path}")
        os.remove(path)

print("[+] Cleanup complete.")

