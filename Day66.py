#Instance Variable and Class Variables in Python

class Employee:
    companyName = "Apple"  #This is class Variable and Cannot be change outside class 
    def __init__(self , name):
        self.name = name 
        self.salary = 2000 #This is Instance Variable and Can be change outside class  

    def showDetail(self):
        print(f"The Salary of {self.name} who work in {self.companyName} is {self.salary}")

emp1 = Employee("Binod")
emp1.showDetail()
emp1.companyName = "Google"  #This has no effect on class

emp2 = Employee("Harry")
emp2.salary  = 3000  #This Effect variable inside class
emp2.showDetail()