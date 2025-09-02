#Rock , Paper , Scissor Game
import random


userContinue = True

print("\n-----Welcome to Rock Paper Scissor Game-----\n\n")

while(userContinue):
    rand_num = (random.random())
    user_input = (input("\nWhat do you choose : ")).title()



    def choose_winner(user , comp):
        print(f"You choose : {user}")
        print(f"Computer Choose : {comp}")

        if user == "Rock":
          if comp == "Paper":
              print("Computer Win")
          else:
              print("You Win")

        elif user == "Paper":
          if comp == "Scissor":
              print("Computer Win")
          else:
              print("You Win")

        else:
          if comp == "Rock":
              print("Computer Win")
          else:
              print("You Win")
        

        
    choose_winner(user_input,"Rock") if rand_num <= 0.33 else choose_winner(user_input,"Paper") if rand_num >0.33 and rand_num<0.66 else choose_winner(user_input,"Scissor")

    user_wish = (input("\nDo you wanna play again ? (Y/N)   ")).upper()
    if(user_wish == "Y"):
       userContinue = True
    else:
       print("\n Thanks for Playing ! \n")
       userContinue = False




