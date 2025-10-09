# MultiLevel Inheritance


class Animal:
    def __init__(self,AnimalName):
        self.AnimalName = AnimalName
    def showDetail(self):
        print(f"The Animal is {self.AnimalName}")

class Dog(Animal):
    def __init__(self ,name,breed):
        self.breed = breed
        self.name = name
        Animal.__init__(self,AnimalName="Dog")


    def showDetail(self):
        Animal.showDetail(self)
        print(f"The Dog Name is {self.name}")
        print(f"The Dog Breed is {self.breed}")
        

class Golden_Retriver(Dog):
    def __init__(self,name,color):
        self.name = name
        self.color = color
        Dog.__init__(self ,name,breed="Golden Retriver"  )


    def showDetail(self):
        Dog.showDetail(self)
        print(f"{self.name} is {self.color}")
        
     
    

Doggy1 = Golden_Retriver("Tommy" , "Black")
Doggy1.showDetail()
