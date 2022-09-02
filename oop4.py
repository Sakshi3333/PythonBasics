class Demo:
    def __init__(self):
        self.A = 10
        self.__B = 20

    def fun(self):
        print("Inside fun")
        print(self.A)
        print(self.__B)

def main():
    obj = Demo
    print(obj.A)
    obj.fun

if __name__ == "__main__":
 main()