#Main for "Check for Palindrome"
#importing function from module > fnModules
from fnModules.checkInput import *
from fnModules.choiceCheck import *
from fnModules.checkPalindrome import *
from fnModules.stringReverser import *

def main():
    #check if wanna check Palindrome
    print("Do you wanna Play Palindrome Check? Y/N ")
    choice=checkYN(input())

    if choice== "y":
        #Input the string to check as palindrome
        inp=checkInput(input())
        output=stringReverse(inp)
        print(output)
        ans=checkPalindrome(inp,output)
        if ans == "Palindrome":
            print("{0} <=> {1} ".format(inp,output))
            print("{0} is a Palindrome".format(inp))
        else:
            print("{0} <!=> {1}".format(inp,output))
            print("{0} is Not a Palindrome".format(inp))
    else:
        print("Game and Check Exiting....")




if __name__ == "__main__":
    main()