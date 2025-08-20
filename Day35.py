# For loop and Else Statements

for i in range(5):
    print(i)

else:
    print("Hey , Loop is Over\n\n")

for i in range(5):
    print(i)
    if(i == 3):
        print("Loop is Breaking and else Statement won\'t be print")
        break;
else:
    print("Hey , I cannot be print because Loop broke ")