# Importing the Morse Code Dictionary for morse code encryption of the string
from morseFns.morseCodeDict import MORSE_CODE_DICT
#morse code convertor from Eng > Morse
def encryptor(msg):
    cipher=""
    for letter in msg:
        if letter != " ":
            cipher += MORSE_CODE_DICT[letter]+" "
        else:
            cipler += " "
    return cipher