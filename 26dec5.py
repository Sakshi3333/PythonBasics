def Addition(*Value):
   sum = 0
   for no in Value:
   
    sum = sum + no
   return sum

def main():
    ret = Addition(10,20,30,40,50)
    print("Addition is :", ret)

    ret = Addition(10,20,30,50)
    print("Addition is :", ret)

    ret = Addition()
    print("Addition is :", ret)
    
if __name__ == "__main__":
    main()