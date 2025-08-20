# Dictionary in Python

my_dict = {
    "name":"binodx",
    "lang":"Python"
}

print(my_dict)
print(my_dict["name"])

# print(my_dict["name2"]) #Gives Error
print(my_dict.get("name2")) #Give none value

#Method 1 to print all key and Values
for key,value in my_dict.items():
    print(f"The {key} is equals to {value}")

#Method 2 to print all Keys and values
for key in my_dict.keys():
    print(f"The {key} is equals to {my_dict[key]}")

