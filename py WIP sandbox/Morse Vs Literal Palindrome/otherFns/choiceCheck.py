def checkYN(x):
    while True:
        if x.lower() in ["y","n","yes","no"]:
            if x.lower in ["y","yes"]:
                return "Y"
                break
            elif x.lower in ["n","no"]:
                return "N"
                break
            else:
                print(" !! > Please enter y / yes, n / no to proceed ...")