from ConvFns.Morse_code_dictionary import *
# For Conversion from english to morse code 
def Encrypt(message):
    cipher=''
    for letter in message:
        if letter != ' ':
            # As character id not space,
            # Look up dictionary to use morse code key:value pair
            cipher += MORSE_CODE_DICT[letter]+' '
            # Add a space after a letter 
        else:
            # Add another space, i.e. 2 spaces after a word
            cipher+=' '

    return cipher
