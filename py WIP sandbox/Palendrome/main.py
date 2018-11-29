#Main for "Check for Palindrome"
#importing function from module > fnModules
from fnModules.choiceCheck import checkYN
from fnModules.checkInput import checkInputString
from fnModules.checkPalindrome import checkPalindrome
from fnModules.stringReverser import stringReverse

def main():
    #check if wanna check Palindrome
    print("Do you wanna Play Palindrome Check? Y/N ")
    choice=checkYN(input())
    # if the palindrome is selected "y" else "N"clear 
    if choice== "y":
        #Input the string to check as palindrome
        print("Please enter the String:")
        inp=input()
        checkInputString(inp)
        output=stringReverse(inp)
        ans=checkPalindrome(inp,output)
        if ans == "Palindrome":
            print("{0} <=> {1} ".format(inp,output))
            print("{0} is a Palindrome".format(inp))
        else:
            print("{0} <!=> {1}".format(inp,output))
            print("{0} is Not a Palindrome".format(inp))
    else:
        print("Game and Check Exiting....")


if __name__ == "__main__" :
    main()
