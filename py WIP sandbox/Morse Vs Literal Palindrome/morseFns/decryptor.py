# Importing the Dictionary for the decryption process
from morseFns.morseCodeDict import MORSE_CODE_DICT
# decryption from morse > Eng
def decryptor(msg):
    msg += " "
    decipher = ""
    ci_text = ""

    for letter in msg:
        if letter != " ":
            i=0
            ci_text += letter

        else:
            i += 1
            if i == 2:
                decipher += " "

            else:
                decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values().index(ci_text))]
    return decipher