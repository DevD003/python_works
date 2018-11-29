def checkPalindrome(x,y,z):
    print(">>> Checking...")
    while True:
        if x.strip() == y.strip() :
            print("{0} <=> {1} ".format(x,y))
            print("{0} is a Palindrome({1})".format(x,z))
            return "{} Palindrome".format(z)
            break
        
        else:
            print("{0} <!=> {1}".format(x,y))
            print("{0} is Not a Palindrome({1})".format(x,z))
            return "Not a {} Palindrome".format(z)
            break