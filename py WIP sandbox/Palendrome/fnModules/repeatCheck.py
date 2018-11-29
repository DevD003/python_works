#function to repeat the round of game if required:
from fnModules.choiceCheck import checkYN
def repeatGame():
    while True:
        print("Would you like to play another round? Y/N")
        choice = checkYN(input())
        if choice == "y":
            return "y"
            continue
        else:
            break
        
