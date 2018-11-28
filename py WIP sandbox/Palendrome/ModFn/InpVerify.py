def verifyString(inp):
    inp=input()
    while True:
        if inp == str(inp):
            print("Entered String......")
            break
        else:
            print("Enter a valid String")
            continue
output=verifyString(input())
print (output)
