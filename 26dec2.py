def Addition(no1, no2):          #function definition
    Ans = 0
    Ans = no1 + no2
    return Ans
def main():
    print("Enter first no:")
    value1 = int(input())

    print("Enter second number:")
    value2 = int(input())

     #keyword arguments
    ret= Addition(no2 =value1, no1 =value2)           #function call
    print("Addition is :",ret)


if __name__ == "__main__":
    main()