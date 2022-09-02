def Division(a,b):
    ans = 0.0
    ans = a/b
    return ans

def SmartDivision(func_name):
    def inner(A,B):
        if A < B:
            A,B = B,A
        return func_name(A,B)

    return inner

Division = SmartDivision(Division)

def main():
    no1 = 0
    no2 = 0

    no1 = int(input("Enter the first number"))
    no2 = int(input("Enter second number"))

    ret = Division(no1,no2)
    print("Division is :", ret)


if __name__ == "__main__":
    main()