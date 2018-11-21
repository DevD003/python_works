# Importing the Dictionary 
from ref_dict.morse_code_dictionary import *
def autoInpClassify(inp):
    inp = input()
    for letter in inp:
        if inp in list(MORSE_CODE_DICT.keys()):
            return "to_encrypt"
        else:
            return "to_decrypt"
        
