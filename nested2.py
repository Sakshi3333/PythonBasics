# 0X100
def fun():
    print("Inside fun")
 # 0X200
def gun(func_name):
    print("Inside gun")
    func_name()        # fun

def main():
    gun(fun)  # 0X100

if __name__ == "__main__":
    main()