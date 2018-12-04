def checkInputString(x):
    while True:
        try:
            x == str(x)
        except:
            print("Enter a valid Word")
            continue
        else:
            print("String Entered...")
            break
    