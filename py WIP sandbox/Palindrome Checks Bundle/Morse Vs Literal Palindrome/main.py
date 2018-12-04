# main() function file for the Morse vs Literal Palindrome
from morseFns.encryptor import *
from morseFns.morseCodeDict import MORSE_CODE_DICT
from otherFns.choiceCheck import * 
from otherFns.repeatGame import *
from palindromeFns.stringRev import *
from palindromeFns.checkPalindrome import *
from palindromeFns.checkInput import *

def main():
    #check if you want to initiate for palindrome check
    print("?? > Do you wanna Try Literal & Morse Palindrome Check: Y/N")
    choice1 = checkYN(input())
    if choice1 == "Y" :
        print(">>> Please enter String: ")
        inp = input ()
        checkInputString(inp)
        output = stringReverse(inp)
        ans = checkPalindrome(inp,output,"Literal")
        print("?? > Do you wanna do Morse Code Wise Palindrome check: Y/N")
        choice2= checkYN(input())
        if choice2 == "Y":
            morse_inp = encryptor(inp.upper())    # entered string conversion to morse code
            rev_morse_inp = stringReverse(morse_inp)
            morse_ans = checkPalindrome(morse_inp,rev_morse_inp, "Morse Wise")
        else:
            print(" !! > Exiting Morse Palindrome Check on String")
        
        choice3=repeatGame()
        if choice3 == "Reload":
            main()
            
    else:
        print(" !! > Game Exiting . . .")

if __name__ == "__main__" :
    main()