from functools import reduce
def CheckEven(no):
    return(no % 2 == 0)
def Increment(no):
    return no + 2
def Addition(no1,no2):
    return no1 + no2
def main():
    data = [5,6,7,8,4]
    print("Original data:", data)

#### filter(function ,list) ##########
    newdata = list(filter(CheckEven, data))
    print("Data after filter:", newdata)

##### map(function , list) ########
    incrementdata = list(map(Increment, newdata))
    print("Data after map: ", incrementdata)

#### reduce(function , list) ###########
    ret = reduce(Addition, incrementdata)

    print("Data after reduce:", ret)

if __name__ == "__main__":
    main()