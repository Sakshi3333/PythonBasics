#2.Write a program which accept N numbers from user and store it into List. Return Maximum 
#number from that List
List = []
num = int(input("How many numbers:"))
for n in range (num):
    num = int(input("Enter the numbers:"))
    List.append(num)
    print("Maximum number from list is:", max(List))