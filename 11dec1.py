def Addition (value1, value2):
    ans = value1 +value2
    return ans

def main():
    print("Marvellous infosytems application")

    no1 = int(input("Enter the first number:"))
    no2 = int(input("Enter second number:"))

    ret = Addition(no1, no2)
    print("Addition is:", ret)

if __name__ == "__main__":
 main()