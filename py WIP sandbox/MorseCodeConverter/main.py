from ConversionMethods. import *
# Main function for process exection or process wise flow 
def main():
    # Input Message to encrypt or decrypt
    print("Enter a message to encrypt or decrypt: ")
    message = input()
    #check input to decide if encryption or decryption required
    output = autoInpClassify(message)

    if output=="to_encrypt":
        result = encrypt(message.upper())
        print("The encryption of message > {0} < is || {1} ||".format(message,result))
    elif output=="to_decrypt":
        result = decrypt(message)
        print("The dencryption of message || {0} || is > {1} <".format(message,result))


if __name__=="__main__":
    main()
