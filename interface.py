import choiceCalc
import data
import roundAuto
import roundRules


RoundRules = roundRules.RoundRules
roundAuto = roundAuto
Data = data.tableCl
Round = choiceCalc.Round

user = Round.GetChoiceInNum()
ai = Round.ChoiceAi()
RoundRules.CheckCasing(user,ai)


