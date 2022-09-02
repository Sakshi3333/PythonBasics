#Write a program which contains one lambda function which accepts one parameter and return 
#power of two
def power (value):
    value = value**2
    return value

powerx = lambda value  :  value**2


def main():
    print("Enter the number:")
    no = int(input())

    ret = power(no)
    print("the power of the number is:", ret)

    ret = powerx(no)
    print("The power of the number using lambda function is :", ret)
   
if __name__ == "__main__":
    main()