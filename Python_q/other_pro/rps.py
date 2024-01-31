import random
l=["Rock","Scissor","Paper"]
class Color:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    RESET = '\033[0m'
def handgame(a):
    usercount=0
    comcount=0
 
 
    for i in range(1,6):
           user=int(input('''select 1 : Rock \nselect 2 : Scissor \nselect 3 : Paper : '''))
           print("\n")
           if(user==1):
               
               userchoise="Rock"
           elif(user==2):
               
               userchoise="Scissor"
           elif(user==3):
               
               userchoise="Paper"
           else:
                  print(Color.RED +"--- Sorry please  choose valid inputs ---"+Color.RESET)
                  handgame(a)


           computer=random.choice(l)
           if(computer == userchoise):
               print(Color.BLUE+"the computer value :" +Color.RESET,computer )
               print(Color.YELLOW+"the user value is : "+Color.RESET,userchoise)
               print(Color.GREEN+"-- GAME DRAW --"+Color.RESET)
               print("\n")
               usercount=usercount+1
               comcount=comcount+1 
           elif((computer=="Rock" and userchoise=="Paper")or(computer=="Paper" and userchoise=="Scissor")
                or(computer=="Scissor" and userchoise=="Rock")):
               print(Color.BLUE+"the computer value : "+Color.RESET,computer)
               print(Color.YELLOW+"the user value is : "+Color.RESET,userchoise)
               print(Color.GREEN+"-- YOU WIN --"+Color.RESET)
               print("\n")
               usercount=usercount+1
           else:
               print(Color.BLUE+"the computer value : "+Color.RESET,computer)
               print(Color.YELLOW+"the user value is : "+Color.RESET,userchoise)
               print(Color.GREEN+"-- COMPUTER WIN -- "+Color.RESET)
               print("\n")
               comcount=comcount+1 

    if(usercount==comcount):
            print(Color.GREEN+"-- FINAL GAME DRAW -- --"+Color.RESET)
            print(Color.BLUE+"the computer win : "+Color.RESET,comcount," times")
            print(Color.YELLOW+"the user value is : "+Color.RESET,usercount," times")
            print("\n")
    elif(usercount>comcount):
            print(Color.GREEN+"-- FINAL YOU WIN -- --"+Color.RESET)
            print(Color.BLUE+"the computer value : "+Color.RESET,comcount," times")
            print(Color.YELLOW+"the user value is : "+Color.RESET,usercount," times")   
            print("\n")
    else:
            print(Color.GREEN+"-- FINAL COMPUTER WIN WIN -- --"+Color.RESET)
            print(Color.BLUE+"the computer value : "+Color.RESET,comcount," times")
            print(Color.YELLOW+"the user value is : "+Color.RESET,usercount," times") 
            print("\n")

 
while True:
    a=int(input("press 1 play game : \npress 2 out the game : "))
    print("\n")
    if(a==1):
         handgame(a)

    else:
         break     