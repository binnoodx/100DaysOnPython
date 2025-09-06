# Inheritance in Python

# Make one class in Python
class EmployeeName:
    def __init__(self , name , id):
        self.name = name
        self.id = id
    def showName(self):
        print(f"Id {self.id} is {self.name}")

#This second class takes all property of first class and extend too
class EmployeeLang(EmployeeName):
    def showLang(self , lang):
        print(f"And he is {lang} programmer")



employee1 = EmployeeLang("BinodX" , 21) #This object is creating on class EmployLang but Employeelang is inherited from first class


employee1.showName()  #Function on Class 1
employee1.showLang("Python") #Function on Class 2