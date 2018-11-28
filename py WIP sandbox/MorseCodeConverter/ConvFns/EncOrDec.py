# Importing the Dictionary 
import ConvFns.Encryptor
import ConvFns.Decryptor
import ConvFns.Morse_code_dictionary

def EncOrDec(self):
    print("please enter 'encrypt' / 'e' or 'decrypt' / 'd'")
    inp = input()
    if (inp == "encrypt" or inp =='e'):
        return "encryption"
    elif (inp == "decrypt" or inp == "d"):
        return "decryption"
    else:
        print("please enter 'encrypt' / 'e' or 'decrypt' / 'd'")