print("SHRI GANESHAYA NAMAH")
print("Demonstration of CLASS")

class Demo:

 def __init__(self,value1,value2):
  print("Inside init method")
  self.i = value1
  self.j = value2

def fun(self):
        print("Inside fun")
        print(self.i,self.j)

def Add(self):
        print(self.i+self.j)

    # CREATE OBJECT OF DEMO CLASS
obj1 = Demo(10,20)

    # CALL THE METHOD FUN
obj1.fun()

    # CREATE OBJECT OF DEMO CLASS
obj2 = Demo(50,60)

    #  CALL THE METHOD FUN
obj2.fun()

    # CALL METHOD ADD TO PERFORM ADDITION OF CHARACTERISTICS
obj1.Add()
obj2.Add()

