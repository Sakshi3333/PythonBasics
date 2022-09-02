class Base:
    def __init__(self):
        self.i = 20
        self.j = 30

    def fun(self):
        print("Base fun")

    def gun(self):
        print("Base gun")

class Derived(Base):
    def __init__(self):
        self.a = 11            # OVERRIDING METHOD
        self.b = 10             # OVERRIDING METHOD

    def fun(self):
        print("Derived fun")

    def sun(self):
        print("Derived sun")
    

def main():
    bobj = Base()
    dobj = Derived()

    dobj.fun()
    bobj.fun()
    dobj.sun()
    dobj.gun()
   

if __name__ == "__main__":
    main()