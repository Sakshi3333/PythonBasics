#Write a program which accept N numbers from user and store it into List. Return addition of all 
#elements from that List.
List = []
num = int(input("How many numbers:"))
for n in range(num):
    num = int(input("Enter the numbers"))
    List.append(num)
    print("Sum of elements in given list:", sum(List))