##WinRansomware

This code should be executed on virtual machines and is intended solely for educational purposes. Hacking is illegal, and I do not endorse any malicious use of this code. This should be used for educational purposes ONLY.

This code creates a ransomware simulation that encrypts files in a specified folder and generates a ransom note asking for payment to decrypt the files.

Key Functions

generate_key(): Generates a new encryption key.


save_key(key): Saves the generated key to a file named secret.key.


load_key(): Loads the encryption key from the secret.key file.


encrypt_file(file, key): Encrypts a given file using the provided key.


decrypt_file(file, key): Decrypts a given file using the provided key.

encrypt_directory(folder, key): Encrypts all files with specific extensions (.txt, .doc, .pdf) in the specified directory.

decrypt_directory(folder, key): Decrypts all files with specific extensions (.txt, .doc, .pdf) in the specified directory.

create_ransom_note(): Creates a ransom note containing a message and contact email for ransom payment instructions.


Main Functionality


The main function orchestrates the following steps:


Defines the path of the folder to be encrypted (/home/user).


Generates a new encryption key and saves it to secret.key.


Encrypts all files in the specified directory.


Creates a ransom note at /home/user/ransom_note.txt.




Deletes the secret.key file to simulate a real ransom scenario where the decryption key is not readily available.




Execution

When the script is run directly, the main function is called, initiating the encryption process and ransom note creation.

Important: This code is a simulation and should be handled responsibly. Use it only in controlled environments to understand ransomware behavior and its implications.
