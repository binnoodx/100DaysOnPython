 # while Loop

# num = 0
# while(num<=5):
#     print(num)
#     num = num +1

# print("Loop Over")

### Guess Number Game ###

number = 69;
guesses = 10;

while(guesses!=0):
    user_inp = int(input("Guess The Number : "))
    if(user_inp == number):
        print("Yay , You won with " , guesses -1 , "guesses left")
        break
    else:
        guesses = guesses-1
        print("Little bit wrong " , guesses , "guesses Left")
else:
    print("Sorry , You Lost")



