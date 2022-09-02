#Demonstration of Filter, Map , Reduce using normal functions #
from functools import reduce
print("SHRI GANESHAYA NAMAH")
print("Demonstration of FILTER,MAP,REDUCE")
def EvenCheck(no):
    return (no %2 == 0)
def Increase (no):
    return no + 2
def Add (a,b):
    return a+b
arr = [8,9,5,16,2,4,21,30,11]
evenArr = list(filter(EvenCheck, arr))
print("Data after filter", evenArr)
ModArray = list(map(Increase,evenArr))
print("Data after map :", ModArray)
sum = reduce(Add,ModArray)
print("Addition of even numbers:", sum)
# Demonstration of FILTER,MAP,REDUCE using lambda function #
evenArr = list(filter(lambda no: (no % 2 == 0),arr))
print("Data after using lambda", evenArr)
ModArray = list(map(lambda no : no+2,evenArr))
print("Data after map using lambda", ModArray)
sum = reduce(lambda a,b:a+b, ModArray)
print("Addition of even numbers using lambda", sum)