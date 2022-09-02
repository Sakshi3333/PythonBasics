print("SHRI GANESHAYA NAMAH")
print("Demonstration of User-defined functions")
######Function which accepts nothing and returns nothing
def Marvellous1():
    print("Inside Marvellous1")
#####Function which accepts value and returns nothing ########
def Marvellous2(value):
    print("Inside Marvellous2")
    print("Accepted value is :", value)
#####Function which accepts value and return value#####
def Marvellous3(value):
    print("Inside Marvellous3")
    print("Accepted value is :", value)
    return value+1
####### Function which accepts multiple value and returns multiple value ########
def Marvellous4(value1,value2):
    print("Inside Marvellous4")
    add = value1 + value2
    sub = value1 - value2
    return add,sub
###### Function which calls another function which is defined outside it ##########
def Marvellous5():
    print("Inside Marvellous5")
    Marvellous1()
###### Function which contains another nested function in it ###########
def Marvellous6():
    print("Inside Marvellous6")
    def InnerFun():
        print("Inside InnerFun")
        InnerFun()
####### Function calls for above functions ###########
no = 30
Marvellous1()
Marvellous2(no)
ret = Marvellous3(no)
print("Return value is :", ret)

Marvellous5()
ret1,ret2 = Marvellous4(10,2)
print("Addition is :", ret1)
print("Substraction is :", ret2)