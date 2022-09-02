class Demo():
    def __init__(self):
        self.A = 10
        self.__B = 20

    def fun():
        print("Inside gun")
        self.__gun()

    def __gun(self):           #PRIVATE METHOD OF CLASS
        print("Inside gun")

def main():
    obj = Demo()
    obj.fun()
   #obj.__gun()

if __name__ == "__main__":
    main()


# A is public
# B IS PRIVATE
#fun is public
#gun is private