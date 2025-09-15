#Class Method as Alternative Constructor

class Employee:
    def __init__(self , name , salary):
        self.name = name
        self.salary = salary

    def showDetail(self):
        print(f"The Salary of {self.name} is {self.salary}") 

    @classmethod
    def fixInput(cls , str): #Takes Class and String as Argument
        return cls(str.split("-")[0] , str.split("-")[1]) #Send the new paramenets again to class of Object emp2


emp1 = Employee("Binod" , 2000) #Name and Salary in Regular Format
emp1.showDetail()

str = "Harry-3000" #Name and Salary in Irregular Format
emp2 = Employee.fixInput(str)
emp2.showDetail()