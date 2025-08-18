#f-strings

##Older Method

line = "Hey ,This is {} and I am learning {}"
name = "BinodX"
lang = "Python"

line.format(name , lang)
print(line)


## Newer Method

line = f"Hey , This is {name} and I am Learning {lang}"
print(line)

## To Print {} in f-strings

print(f"We use f\"{{}}\" to use f-strings")

