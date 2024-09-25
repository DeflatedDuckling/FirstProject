import RoundSystem.choiceCalc as choiceCalc 
import RoundSystem.roundRules as roundRules

class RoundSystem :
    def __init__(self) -> None:
        pass
    
    def Create_Class(max) :
        i = 0
        while (i < max) :
            i = i + 1
            a = choiceCalc.Round
            b = a.Get_Choice()
            c = a.Choice_Ai()
            check = roundRules.RoundRules
            e = check.CheckCasing(b,c)
        return "True"
            