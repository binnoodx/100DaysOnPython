#Getters and Setters in Python

class myClass:

    def __init__(self , num):
        self.NewNum = num
    @property
    def ten_times(self):
        return self.NewNum *10
    @ten_times.setter

    def ten_times(self , finalNum):
        pass



obj = myClass(20)
print(obj.ten_times)
