#Magic Keywords in Python

class Employee:
    def __init__(self , name , salary):
        self.name = name
        self.salary =salary


    
    #__call__ makes Object callable
    def __call__(self):
        print(f"Employee {self.name} has salary {self.salary}")

    def __len__(self):
        i=0
        for character in self.name:
            i=i+1    
        return i



emp1 = Employee("Harry" , 20000)
emp1()

print(len(emp1)) #Since emp1 is object and we cannot find its length
