# CLASS DEFINITION
class  Arithmatic:
  def __init__(self,a,b):     #CONSTRUCTOR
    print("Inside init (Constructor)")
    self.no1 = a          #CHARACTERISTICS
    self.no2 = b          #CHARACTERISTICS

  def Addition(self):    #BEHAVIOUR
    ans = self.no1 + self.no2
    return ans

def main():
   print("Enter first number:")
   x = int(input())

   print("Enter second number:")
   y = int(input())

   obj = Arithmatic(x,y)
   ret = obj.Addition()

   print("Addition is:", ret)

if __name__ == "__main__":
  main()