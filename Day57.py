#Object and Classes in Python

#Declaring Class
class employee:
    name = "employee_name" #Default Name for any Object
    lang = "employee_lang" #Default Name for any Object
    def info(self):  #Self keyword makes sure that function run for those object which has called it
        print(f"{self.name} is {self.lang} developer")

#Creating Object
emp1 = employee()
emp1.name = "Binod"
emp1.lang = "Python" #We can access like this
emp1.info() # emp1 calls info function so self make sure that info function run for emp1 object

#Creating another object
emp2 = employee()
emp2.name = "Harry"
emp2.lang = "Java"
emp2.info()