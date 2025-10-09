#MultiLevel Inheritance

class Employee:
    def __init__(self,name):
        self.name = name

    def show(self):
        print("Showed From Employee Class")

class Dancer:
    def __init__(self,dance):
        self.dance = dance

    def show(self):
        print("Showed From Employee Class")

class DancerEmployee(Employee,Dancer): ## Since Employee Class is Before Dancer Class , Show function will be run from Employee Class

    def __init__(self):
        pass
        

Emp1 = DancerEmployee()
Emp1.show()

print(DancerEmployee.mro()) #Print where the class find function in sequence

