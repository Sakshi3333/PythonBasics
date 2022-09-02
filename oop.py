# ENCAPSULATION - CLASS = CHARACTERISTICS + BEHAVIOUR
class Arithmetic:       #CLASS DEFINITION
    def __init__(self,a,b):    #CONSTRUCTOR
     print("print Inside init(Construtor)")
     self.no1 = a             #CHARACTERISTICS
     self.no2 = b             #CHARACTERISTICS

    def Addition(self):        #Behaviour
        ans = self.no1 + self.no2
        return ans

def main():
    print("Enter first number:")
    x = int(input( ))

    print("Enter second number:")
    y = int(input())

    obj = Arithmetic(x,y)     #OBJECT CREATION
    ret = obj.Addition()

    print("Addition is :" , ret)

if __name__=="__main__":
    main()