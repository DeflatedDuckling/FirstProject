import RoundSystem.choiceCalc as choiceCalc
import Data.data as data
import RoundSystem.roundAuto as roundAuto
import RoundSystem.roundRules as roundRules


RoundRules = roundRules.RoundRules
roundAuto = roundAuto
Data = data.tableCl
Round = choiceCalc.Round

RoundS = roundAuto.RoundSystem
auto = RoundS.CreateClass(3)