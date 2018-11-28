from ConvFns.EncOrDec import EncOrDec
from ConvFns.Encryptor import Encrypt
from ConvFns.Decryptor import Decrypt
from ConvFns.VerifyConv import *
# Main function for process exection or process wise flow 
def main():
    # Input Message to encrypt or decrypt
    print("Enter a message to encrypt or decrypt: ")
    message = input()
    #check input to decide if encryption or decryption required
    
    output=EncOrDec(message)
    
    if output=="encryption":
        result = Encrypt(message.upper())
        print("The encryption of message > {0} < is || {1} ||".format(message,result))
    elif output=="decryption":
        result = Decrypt(message)
        print("The dencryption of message || {0} || is > {1} <".format(message,result))

    YN=VerifyConv_YN(output)
    
    VerifyConv (YN,output,message,result)
    

if __name__=="__main__":
    main()
