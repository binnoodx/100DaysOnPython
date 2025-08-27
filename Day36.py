#Error Handlings


num = input("Enter Any Valid Integer : ")

try:
    for i in range(int(num)):
        print("Yay , You have Entered a Valid Integer")

except:
    print("Sorry , You didn't provide Integer")