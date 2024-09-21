import RoundSystem.choiceCalc as choiceCalc
import Data.data as data
import RoundSystem.roundAuto as roundAuto
import RoundSystem.roundRules as roundRules


RoundRules = roundRules.RoundRules
roundAuto = roundAuto
Data = data.tableCl
Round = choiceCalc.Round

user = Round.GetChoiceInNum()
ai = Round.ChoiceAi()
RoundRules.CheckCasing(user,ai)


