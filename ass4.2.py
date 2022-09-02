#Write a program which contains one lambda function which accepts two parameters and return 
#its multiplication.
Multiplication = lambda a , b : a*b

def main():
    ret = Multiplication(4,3)
    print("Multiplication is :", ret)

if __name__ == "__main__":
    main()