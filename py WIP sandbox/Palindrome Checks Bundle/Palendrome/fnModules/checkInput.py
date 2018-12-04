
# Function to check if the argument is string
def checkInputString (x):
    while True:
        try:
            x==str(x)
        except:
            print("Enter a Valid String")
            continue
        else:
            print("String Entered...")
            break

