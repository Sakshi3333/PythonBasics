#3.Write a program which accept N numbers from user and store it into List. Return Minimum 
#number from that List.
List = []
num = int(input("How many numbers:"))
for n in range(num):
    num = int(input("Enter the numbers:"))
    List.append(num)
    print("Minimum number from list is :", min(List))