# Importing the Dictionary 
import encryptor
import decryptor
import morse_code_dictionary

def encOrDec(self):
    print("please enter 'encrypt' / 'e' or 'decrypt' / 'd'")
    inp = input()
    if (inp == "encrypt" or inp =='e'):
        return "encryption"
    elif (inp == "decrypt" or inp == "d"):
        return "decryption"
    else:
        print("please enter 'encrypt' / 'e' or 'decrypt' / 'd'")