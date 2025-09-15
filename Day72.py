# Super Keyword In Python

class Employee:
    def __init__(self , name , salary):

        self.name = name
        self.salary = salary

    def showDetails(self):        
        print(f"Employee {self.name} has salary {self.salary}")

        

class Programmer(Employee):
    def __init__(self ,name, salary, lang):
        super().__init__(name , salary)  #This super().__init__() is the function of Parent class -->Emplayee
        self.lang = lang


emp1 = Employee("Binod" , 2000)
emp1.showDetails()

emp2 = Programmer("Harry" , 3000 , "Python")
emp2.showDetails()
        

        