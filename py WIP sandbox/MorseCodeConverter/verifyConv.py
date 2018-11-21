# Importing the dictionary 
from morse_code_dictionary import *
from encryptor import *
from decryptor import *

# Verify encryption or decryption performed 
def verifyConv_YN(output):
    while True:
        print("Do you wanna Verify the conversion? Y/N")
        x=input()
        if (x.upper() == "Y" or x.upper() =="N"):
            if x.upper() == 'Y':
                print("Verifying the {} .....".format(output))
                return "Y"
                break
            else:
                print("Verifying the {} .....".format(output))
                return "N"
                break
        else:
            print("Please enter 'Y' or 'N'")
            x=input()
            continue

def verifyConv(YN,output,result):
    while True:
        if YN == "Y" and output in ["e","encryption"]:
            print("Decrypting >>> {}".format(result))
            print(decrypt(result))
            break
        elif YN == "Y" and output in ["d","decryption"]:
            print("Encrypting >>> {}".formst(result))
            print(encrypt(result))
            break
        else:
            print("Verification --- Not Opted ---")
            break
            
    