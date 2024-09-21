import math
import data
import random
import roundRules

class Round :
    def __init__(self) -> None:
        pass
    
    def GetChoiceInNum() :
        print(" 1 = Rock, 2 = Paper, 3 = Scissors")
        choice = int(input("Enter your choice: "))
        match choice: ## THIS LOOKS a little better -- Just a little better.
            case 1:
                print("Rock")
                return 1
            case 2:
               print("Paper")
               return 2
            case 3:
                print("Scissors")
                return 3
            case _default :
              raise ValueError("You are worse than a stone tablet")
        
    def ChoiceAi() :
        aiAnswer = random.randint(1,3)
        match aiAnswer:
            case 1:
                print("AI chooses " + "Rock")
            case 2:
                print("AI chooses " + "Papers")
            case 3:
                print("AI chooses " + "Scissors")
                
        return aiAnswer


