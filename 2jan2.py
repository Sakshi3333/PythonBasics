class Demo:
    A = 10
 
    def __init__(self):
        print("Inside (Constructor):")
        self.B = 20
    
    def fun_instance(self):
        print("Inside Instance method")
        print(self.B)
        print(self.A)
        print(Demo.A)

@classmethod
def fun_class(cls):
    print("Inside class method") 
    print(cls.A)  
    print(Demo.A)     #CLASS METHOD
    
@staticmethod
def fun_static():
        print("Inside static method")        #STATIC METHOD

def __del__(self):
        print("Inside (Destructor):")

def main():
    
    obj = Demo()                             #OBJECT CREATION
    obj.fun_instance()

    
        
if __name__ == "__main__":
   main()
    