print("SHRI GANESHAYA NAMAH")
print("Demonstration of Datatypes")
no = None
print(None)
print(type(None))
print(id(no))

no = 11
print(no)
print(type(no))
print(id(no))
########################################################
no = 11                   #int
print(type(no))
no = 3.14               #float
print(type(no))
no = 6+3j                 #complex
print(type(no))
no = True
print(type(no))        #boolean
#################################################
#we can convert one variable from one datatype to another datatype(typecasting)
no = 30
no = float(no)
print(no)
print(type(no))
print(type(id))

no = 3.14
no = int(no)
print(no)
print(type(no))
print(type(id))

a = 5
b = 6
no = complex(a,b)
print(no)
print(type(no))
print(type(id))
###################################################################################
#Under sequence there are different datatypes as List,Set,Tuple,Range
ListX = [10,20,30,40]
print(ListX)
print(type(ListX))

Set = {10,20,30,40}
print(Set)
print(type(Set))

TupleX = (10,20,30,40)
print(TupleX)
print(type(TupleX))

name = "Sakshi"
print(name)
print(type(name))

ex = list(range(1,10))
print(ex)
print(type(ex))

ex1 = list(range(1,20,2))
print(ex1)
print(type(ex1))
###########################################################################################
#Dictionary contains key and value
batches ={"IT":"9000","DSA":"3000","PL":"2000"}
print(batches)
print(type(batches))
print(batches.keys())
print(batches.values())
print(batches["IT"])