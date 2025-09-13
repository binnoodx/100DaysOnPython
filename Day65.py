#Static Methods in Python

class Math:
    def __init__(self , num1 , num2):
        self.num1 = num1
        self.num2 = num2

    #This Function needs self as argument
    def add1(self):
        return self.num1 + self.num2
    
    @staticmethod
    #This Function lie inside the class but no need to use self as arguments
    def add2(a,b):
        return a +b
    
obj1 = Math(1,2)
print(obj1.add1())

print(Math.add2(1,2))

