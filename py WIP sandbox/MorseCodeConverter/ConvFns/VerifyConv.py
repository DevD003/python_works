# Importing the dictionary 
from ConvFns.Morse_code_dictionary import *
from ConvFns.Encryptor import *
from ConvFns.Decryptor import *

# Verify encryption or decryption performed 
def VerifyConv_YN(output):
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

def VerifyConv(YN,output,message,result):
    while True:
        if YN == "Y" :
            if (output == "encryption"):
                print("Decrypting {0} >>> {1}".format(message,result))
                break
            elif (output == "decryption"):
                print("Encrypting {0} >>> {1}".format(message,result))
                break
        else:
            print("Verification --- Not Opted ---")
            break
            
    