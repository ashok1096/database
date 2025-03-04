from cryptography.fernet import Fernet
import os

# Clears up the user interface
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Encryption function
def run_encryption():
    input('   Here you will be able to Encrypt a file\n\nPress Enter to continue')
    
    while True:
        DYH = input('Do you have your own encryption key? y/n: ').strip().lower()
        print('-----------------------')
        if DYH == 'y':
            P_keyfile_name = input('Type the key file name here: ').strip()
            print('-----------------------')
            try:
                with open(P_keyfile_name, 'rb') as mykey:
                    P_keyfile_name = mykey.read()
            except FileNotFoundError:
                print(f"Error: The key file '{P_keyfile_name}' was not found.")
                continue

            file_name = input('What file would you like to encrypt? ').strip()
            print('-----------------------')
            try:
                with open(file_name, 'rb') as original_file:
                    original = original_file.read()
            except FileNotFoundError:
                print(f"Error: The file '{file_name}' was not found.")
                continue

            try:
                pek = Fernet(P_keyfile_name)
            except ValueError:
                print("Error: Invalid encryption key format.")
                continue

            encrypted = pek.encrypt(original)

            while True:
                copy_ver = input('Do you want the encrypted file to make an un-encrypted copy? y/n: ').strip().lower()
                print('-----------------------')
                if copy_ver == 'y':
                    with open('Encrypted_' + file_name, 'wb') as encrypted_file:
                        encrypted_file.write(encrypted)
                    print('Your file has been encrypted.')
                    input('Press Enter to go back to the main menu')
                    clear()
                    return
                elif copy_ver == 'n':
                    with open(file_name, 'wb') as encrypted_file:
                        encrypted_file.write(encrypted)
                    print('Your file has been encrypted.')
                    input('Press Enter to go back to the main menu')
                    clear()
                    return
                else:
                    print('ERROR! You have to type y or n.')
        elif DYH == 'n':
            print('You need an encryption key to encrypt a file.\nPlease create one using option 4 in the main menu.')
            input('Press Enter to leave')
            clear()
            return
        else:
            print('ERROR! You have to type y or n. Anything else will result in this error message.')
