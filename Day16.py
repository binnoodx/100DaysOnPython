
# Match Case In python

num = int(input("Enter Any Number : "))

match num:
    case 0:
        print("You Entered 0")
    
    case 1:
        print("You Entered 1")

        # --- Case _ works for every value if consitions meets

    # case _ if num:
    #     print("You Entered ", num)
    
    case _ if num != 20:
        print("You Have Entered " , num, "which is not 20")