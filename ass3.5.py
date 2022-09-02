#5.Write a program which accept N numbers from user and store it into List. Return addition of all 
#prime numbers from that List. Main python file accepts N numbers from user and pass each 
#number to ChkPrime() function which is part of our user defined module named as 
#MarvellousNum. Name of the function from main python file should be ListPrime(). 
ListPrime = []
num = int(input("How many numbers:"))
for n in range(num):
    num = int(input("Enter the numbers"))
    ListPrime.append(num)
    if num > 1:
        for i in range(2, int(num/2)+1):
            if (num % i) == 0:
                print(num, "is not a prime number")
                break
            else:
                print(num, "is a prime number")
print("Sum of  the numbers:", sum(ListPrime))
    