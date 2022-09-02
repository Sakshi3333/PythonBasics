#default arguments
def Area(radius, PI = 3.14):          #function definition
    Ans = 0
    Ans = PI * radius *radius
    return Ans

def main():
    print("Enter radius of circle:")
    value = float(input())

    ret = 0.0
   # ret = Area(value)
    ret = Area(PI = 7.10, radius =  value)
    print("Area of circle is:", ret )

if __name__ == "__main__":
    main()