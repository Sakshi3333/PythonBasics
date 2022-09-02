class Demo:
    def __init__(self):
        self.A = 10
        self.__B = 20

    def fun(self):
        print("Inside fun")
        self.__gun()
        
    def gun(self):
        print("Inside gun")

def main():
    obj = Demo
    obj.fun
    obj.__gun

if __name__ == "__main__":
 main()