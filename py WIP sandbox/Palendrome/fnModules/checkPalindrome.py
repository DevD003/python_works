
#Funtion to check for if the string is a palidrome 

def checkPalindrome(string,rev_str):
    while True:
        if string.strip() == rev_str.strip():
            return "Palindrome"
            break
        else:
            return "Not-Palindrome"
            break