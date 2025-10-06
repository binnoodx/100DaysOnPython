#Single Level Inheritance

class Animal:
    def __init__(self,name):
        self.name = name
    
    def make_sound(self):
        return (f"Sound made by {self.name}")

class Dog(Animal):
    def __init__(self, name):
        Animal.__init__(self,name)
    
    def make_sound(self):
        return("Bark, Bark !!!") #Method Overwriting

cat  = Animal("Billi")
print(cat.make_sound())
  
dog = Dog("Kutta")
print(dog.make_sound())