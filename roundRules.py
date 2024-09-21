class RoundRules :
    def __init__(self) -> None:
        pass
    def CheckCasing(user, ai) :
       match user:
           case user if user == ai:
               print("Tie")
               return 0
           case user if user == 1 and ai == 2:
               print("Win")
               
           case user if user == 2 and ai == 1:
               if(ai == 3):
                   print("Lose")
               print("Win")           
               
           case user if user == 3 and ai == 2:
               if(ai == 1) :
                   print("Lose")
               print("Win")
               
    