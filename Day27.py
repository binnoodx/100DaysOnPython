#KBC
print("--- Welcome to KBC ---")

questions = ["Which of the following Language is not OOPS?" , "What is correct print Statement in Python?","Which company does Facebook Belongs?"]

# o_1ptionsForQue = {"opt1":"Java" , "opt2":"Python" , "opt3":"C++" ,"opt4":"C"}
# o_2ptionsForQue2 = {"opt1":"print()" , "opt2":"System.out.println()" , "opt3":"printf()" ,"opt4":"console.log()"}
# o_3ptionsForQue3 = {"opt1":"Apple" , "opt2":"Google" , "opt3":"Meta" ,"opt4":"Amazon"}

o1 = ["Java" , "Python" , "C++" , "C"]
o2 = ["print()" , "System.out.println()" , "printf()" , "console.log()"]
o3 = ["Apple" , "Google" , "Meta" , "Amazon"]



answers = ["d","a","c"]


Question_no = 0
isUserPlayable = True
user_cash = 0

for question in range(0, len(questions)):

    

    while(isUserPlayable!=False):

        Question_no = Question_no +1


        print("Question :" , questions[Question_no-1])


        print("Options : \n")

        


        
        



        user_inp = str(input("Enter Answer : "))
        print("User Input " , user_inp.lower())

        if(user_inp.lower() == answers[Question_no-1]):
            print("Your Answer is Correct")
            user_cash = user_cash + 100
            print("Your Total Cash is " , user_cash)
            isUserPlayable = True

        else:
            print("Your answer is Incorrect and You are taking ",user_cash," with You!")
            isUserPlayable = False
            

        print("\n\n")
            
            

        


        
        
                
    

        
        


    