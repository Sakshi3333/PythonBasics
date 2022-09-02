print("SHRI GANESHAYA NAMAH")
print("Demonstration of strings")
name = "Marvellous"
print(name)
print(type(name))
Newname = "Marvellous"
print(Newname)
print(type(Newname))

print(name[0])
print(name[9])
#print(name[10]) OUT OF RANGE

######### negative index accesses from right to left  ###########
print(name[-1])
print(name[-2])
print(name[-3])

# WE can also print characters in range
print(name[0:3])
print(name[1:2])
print(name[1:6])
print(name[:2])
print(name[3:])

# Strings in python are immutable #
#name[0] = 'm'

# len function is used to calcluate the length of string #
print(len(name))

#STRIP method removes whitespaces from beginning and end #
clasName = "   Marvellous infosytems pune    "
print(clasName.strip())

# Using string we can tokanize the string
Batches = "ppa,lb,unix,python,angular,pl"
print(Batches.split(","))