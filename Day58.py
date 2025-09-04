# Constructors in Python

class employee:

    # Initalizing Function
    def __init__(self , name , lang):

        self.employeeName =name
        self.employeeLang = lang
    
    def info(self):
        print(f"{self.employeeName} is {self.employeeLang} Developer")
        

#No need to write like emp1.name="Binod" , emp1.lang="Python"

emp1 = employee("Binod" , "Python") #We are seeing 2 parameters but it is sending 3 parameters including emp1 as self

emp2 = employee("Harry","Java")

emp1.info()
emp2.info()

