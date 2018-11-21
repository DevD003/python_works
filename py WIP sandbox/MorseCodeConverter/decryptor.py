# Importing the morse code dictionary
from morse_code_dictionary import *

# Function for the decryption from Morse code to English
def decrypt(morse_message):
    # Adding a space at end of morse code for EOS finding
    morse_message+=" "
    # Deciphered Morse code will be saved as string here 
    decipher=" "
    # Per Word Cipher text will be assigned to var
    ci_text=" "

    #deciphering the morse code
    for letter in morse_message:
        #if it is not a space, add it to Ci_text
        if letter != " ":
            #keepin a count of spaces from var i
            i=0
            ci_text+=letter
        else:
            i+=1
            #if i = 2 then two spaces consecutively occured, so add space
            if i==2:
                ci_text+=" "
            #if i!= 2 then the word with space is done, add to decipher
            else:
                decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values().index(ci_text))]
                #Adding the word in english from refering keys to the values with index of Ci_text
    return decipher 

