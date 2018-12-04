# Importing the Morse Code Dictionary for morse code encryption of the string
from morseFns.morseCodeDict import *
#morse code convertor from Eng > Morse
def encryptor(msg):
    cipher=""
    for letter in msg:
        if letter != " ":
            cipher += MORSE_CODE_DICT[letter] 
        
    return cipher