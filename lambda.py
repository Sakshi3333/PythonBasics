print("SHRI GANESHAYA NAMAH")
print("Demonstration of lambda:Anonymous function")
#Defining regular function
def Add(value1 , value2):
    return value1 + value2
value1 = 11
value2 = 10
ret = Add(value1, value2)
print("Addition is {} with the regular function".format(ret))

# Defining lambda function ie anonymous function
fp = lambda no1,no2 : no1 + no2
ret = fp(value1 , value2)
print("Addition is {} with lambda function".format(ret))