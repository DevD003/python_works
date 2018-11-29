# main() function file for the Morse vs Literal Palindrome
from morseFns import *
from otherFns import *
from palindromeFns import *

def main():
    #check if you want to initiate for palindrome check
    print("?? > Do you wanna Try Literal vs Morse Palindrome Check: Y/N")
    choice1 = checkYN(input())
    if choice1 == "Y":
        print(">>> Please enter String: ")
        inp = input ()
        checkInputString(inp)
        output = stringReverser(inp)
        ans = checkPalindrome(inp,output,"Literal")
        print("?? > Do you wanna do Morse Code Wise Palindrome check: Y/N")
        choice2= checkYN(input())
        if choice2 == "Y":
            morse_inp = encrypt(inp)    # entered string conversion to morse code
            morse_out = encrypt(output) #reversed string conversion to morse code
            morse_ans = checkPalindrome(morse_inp,morse_out, "Morse Wise")
        else:
            print(" !! > Exiting Morse Palindrome Check on String")
        
            
    else:
        print(" !! > Game Exiting . . .")

if __name__ == "__main__" :
    main()