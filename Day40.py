## Secret Word Coding and Decoding
#Secret Code Language
import random
def coding(user_word):
    if(len(user_word)>=3):

        for i in range(3):

            randomNumber1 = random.randrange(0,25)
            randomNumber2 = random.randrange(0,25)
            randomNumber3 = random.randrange(0,25)
            randomNumber4 = random.randrange(0,25)
            randomNumber5 = random.randrange(0,25)
            randomNumber6 = random.randrange(0,25)

        codeWord = letters[randomNumber1]+letters[randomNumber2]+letters[randomNumber3]+user_word.split(user_word[0])[1] + user_word[0]+letters[randomNumber4]+letters[randomNumber5]+letters[randomNumber6]
        


        print(f"Your Coded Word is {codeWord}")
        
        
    else:
        print()



def decoding(user_word):
    print()

    temp1 = user_word[3:len(user_word)-3]
    last_letter = temp1[len(temp1)-1]

    final_word = last_letter+temp1[0:len(temp1)-1]
    print(f"Your Deoded Word is {final_word}")





user_word = input("Enter Message : ")
letters = "abcdefghijklmnopqrstuvwxyz"
user_input = input("Enter D for Decoding and C for Coding : ")


if(user_input == "D"):
    decoding(user_word)
else:
    coding(user_word)


