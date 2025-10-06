#Method Overloading in Python

class Vector:
    def __init__(self,i,j,k):

        self.i=i
        self.j=j
        self.k=k

    #Since  Python don't know Vector Addition , We made our own operator
    def __add__(self,vec2):
        return f"{self.i+vec2.i}i + {self.j+vec2.j}j + {self.k+vec2.k}k"
    
vec1 = Vector(1,2,3)
vec2=Vector(4,5,6)
print(vec1+vec2)  #We made our custom add operator according to our use and overload exixting one