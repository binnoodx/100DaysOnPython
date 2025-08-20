#set Methods in Python

s1 = {1,2,3,4}
s2 = {3,4,5,6}

print(s1.union(s2))
print(s1.intersection(s2))
print(s1.isdisjoint(s2))
print(s1.symmetric_difference(s2)) # s1 union s2 - s2 intersection s2
print(s1.difference(s2)) #S1-S2

s3 = {1,2}
s4 = {1,2,3,4}
print(s3.issuperset(s4))
print(s3.issubset(s4))

s1.remove(10)  #Gives Error when particulae element don't meet
s2.discard(10) # Same as remove but don't gives error

print(s1.pop()) #Gives Random Element of Set



s1.clear() #Clear Entire set

del s1 #Delete Entire set
