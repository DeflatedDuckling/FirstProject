import moves

class RoundRules :
    def __init__(self) -> None:
        pass
    def CheckCasing(user, ai) :
       print("Ran")
       match user:
           case user if user == ai:
               print("Tie")
               return 0
        
           case user if user == moves.rock and (ai == moves.scissors or ai == moves.paper):
               if(ai == moves.paper) :
                   print("Lose")
                   return 1
               print("Win")
               return -1
           
           case user if user == moves.paper and (ai == moves.scissors or ai == moves.rock) :
               if(ai == moves.rock) :
                   print("Win")
                   return 1
               print("Lose")
               return -1
           
           case user if user == moves.scissors and (ai == moves.paper or ai == moves.rock) :
               if(ai == moves.rock):
                   print("Lose")
                   return -1
               print("Win")
               return 1
           
               
    