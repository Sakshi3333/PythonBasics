class Demo():
    def __init__(self):
        self.i = 10
        self.j = 20


    def Add(self,a):                                # METHOD OVERLOADING
        print("Inside add with one parameter")       #
                                                    #
    def Add(self,a,b):                                #
        print("Inside add with two parameter")       # METHOD OVERLOADING

def main():
    obj = Demo()
    #obj.Add(11)
    obj.Add(11,21)

if __name__ == "__main__":
    main()