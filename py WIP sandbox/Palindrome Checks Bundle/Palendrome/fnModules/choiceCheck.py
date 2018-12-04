def checkYN(x):
    while True:
        if x.lower() in ["y", "n", "yes", "no"]:
            if x.lower() in ["y", "yes"]:
                return "y"
                break

            else:
                return "n"
                break
        else:
            print("Please enter Y or N, yes or no")
inp = input()