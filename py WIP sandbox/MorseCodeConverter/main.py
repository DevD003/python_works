from encOrDec import encOrDec
from encryptor import encrypt
from decryptor import decrypt
from verifyConv import *
# Main function for process exection or process wise flow 
def main():
    # Input Message to encrypt or decrypt
    print("Enter a message to encrypt or decrypt: ")
    message = input()
    #check input to decide if encryption or decryption required
    
    output=encOrDec(message)
    
    if output=="encryption":
        result = encrypt(message.upper())
        print("The encryption of message > {0} < is || {1} ||".format(message,result))
    elif output=="decryption":
        result = decrypt(message)
        print("The dencryption of message || {0} || is > {1} <".format(message,result))

    YN=verifyConv_YN(output)
    
    verifyConv (YN,output,result)
    

if __name__=="__main__":
    main()
