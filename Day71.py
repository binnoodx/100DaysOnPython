# Dir() , __dict__ and help() in Python

#dir()
my_list = [1,2,3]
print(dir(my_list)) #Give all methods associated with my_list


#__dict__
class Employee:
    def __init__(self , name , salary):
        self.name = name
        self.salary = salary

    def showDetail(self):
        print(f"The Salary of {self.name} is {self.salary}") 


emp1 = Employee("Binod" , 2000) 
emp1.showDetail()

print(emp1.__dict__) #give all parameters of emp1 in dict format

#help()
 
print(help(int)) #Give Documentation on given Keyword