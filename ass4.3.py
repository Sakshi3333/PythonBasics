#3.Write a program which contains filter(), map() and reduce() in it. Python application which 
#contains one list of numbers. List contains the numbers which are accepted from user. Filter 
#should filter out all such numbers which greater than or equal to 70 and less than or equal to 
#90. Map function will increase each number by 10. Reduce will return product of all that 
#numbers.
from functools import reduce
def CheckNum(no) :
    return (no >= 70 > 90)
def Increment(no):
    return no+10
def Addition(no):
   return no
def main():
    List = []
    print("Original data is", List)

List = []
no = int(input("How many numbers:"))
for n in range():
    no = int(input("Enter the numbers:"))
    List.append(no)
# filter(function,list)
newList = list(filter(CheckNum, List))
print("List after filter:", List)
# map(function, list)
incrementnum = list(map(Increment,newList))
print("List after map:", incrementnum)
# reduce(function, list)
ret = reduce(Addition, incrementnum)
print("Data after reduce:", ret)

if __name__ == "__main__":
    main()

