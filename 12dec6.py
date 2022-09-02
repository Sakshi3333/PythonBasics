def Arithmetic (no1, no2):
    add = no1 + no2
    sub = no1 - no2
    return add,sub

def main():
 print("Enter the first number:")
no1 = int(input())

print("Enter the second number:")
no2 = int(input())

ret1, ret2 = Arithmetic (no1,no2)

print("Addition is :", ret1)
print("Substraction is :", ret2)

if __name__ == "__main__":
    main()
