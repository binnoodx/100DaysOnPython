#Access Modifier

class Hey:
    def __init__(self):
        # self.name = "BinodX" #Public
        self.__name = "BinodX" #Private but still accessable

obj1 = Hey()
print(obj1.name) #Give Error when self.__name = "BinodX"
print(obj1._Hey__name)
