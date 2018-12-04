from otherFns.choiceCheck import checkYN
def repeatGame():
    print("?? > Do You Wanna Start Again: Y/N ")
    option = checkYN(input())
    if option == "Y":
        print(" !! > Reloading Game...")
        return "Reload"
    else:
        print(" !! > Closing & Exiting Game...")

    