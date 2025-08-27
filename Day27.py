print("--- Welcome to KBC ---")

questions = [
  [
    "Which Company Own Facebook ?" , "Amazon" , "Meta" , "Apple" , "Google" , 2
  ],
  [
    "Who is the founder of Microsoft?" , "Steve Jobs" , "Bill Gates" , "Mark Zuckerberg" , "Elon Musk" , 2
  ],
  [
    "What does CPU stand for?" , "Central Processing Unit" , "Computer Personal Unit" , "Control Processing Unit" , "Central Program Utility" , 1
  ],
  [
    "Which programming language is used for web styling?" , "HTML" , "CSS" , "Python" , "C++" , 2
  ],
  [
    "Who is known as the father of the Internet?" , "Tim Berners-Lee" , "Vinton Cerf" , "Dennis Ritchie" , "James Gosling" , 2
  ],
  [
    "What year was JavaScript created?" , "1991" , "1995" , "2000" , "1989" , 2
  ],
  [
    "Which company developed the iPhone?" , "Samsung" , "Apple" , "Nokia" , "Google" , 2
  ],
  [
    "What does AI stand for?" , "Artificial Integration" , "Advanced Internet" , "Artificial Intelligence" , "Automated Information" , 3
  ],
  [
    "Which is the most widely used database?" , "MongoDB" , "MySQL" , "Firebase" , "Redis" , 2
  ],
  [
    "Who created Linux?" , "Linus Torvalds" , "Richard Stallman" , "Dennis Ritchie" , "Bjarne Stroustrup" , 1
  ],
  [
    "What does HTTP stand for?" , "HyperText Transfer Protocol" , "High Transfer Text Program" , "Hyperlink Transfer Protocol" , "HyperText Transmission Path" , 1
  ]
];

# print(questions[1][0])
user_cash = 0
gameOver = False
for question in questions:
    
    hasAnswered = False

    while(hasAnswered != True and gameOver == False):
        print("The Question is ",question[0],"\n")
        print("Your Options Are \n")
        for i in range(1,5):
            print(question[i],"  ")
        user_input = int(input("Choose 1/2/3/4  -> "))

        if(user_input == question[5]):
            print("Correct Answer \n")
            user_cash = user_cash +100;
            hasAnswered = True
        else:
            print("Wrong Answer and You are Out \n")
            gameOver = True




print(f"Game Over and You won {user_cash}")

