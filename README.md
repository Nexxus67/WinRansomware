# WinRansomware
This should be executed on virtual machines, and it's for educational purposes. Hacking is illegal and I do not endorse any evil use of this code. This should be used for educational purposes ONLY. 


This code creates a ransomware that encrypts files in specified folders and creates a ransom note to be displayed to the victim asking for payment to decrypt the files.

The create_ransomware function takes a list of folders to be encrypted and generates a new encryption key for each folder. It then encrypts all files in the folder using the generated key and writes a ransom note in each folder asking for payment to decrypt the files. The ransom note contains an email address to contact for instructions on how to pay the ransom and get the decryption key.

The ransom_note function creates a text file called "RANSOM_NOTE.txt" on the victim's desktop, containing the message that the victim has been infected with ransomware, and instructions on how to pay the ransom.

The main function calls the create_ransomware function. Finally, the code checks if the script is being run directly and if so, calls the main function to execute the code.
