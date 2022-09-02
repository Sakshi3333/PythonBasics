#### OOP4 ######
class Demo:
    def __init__(self):
        print("Inside (Constructor):")

    def __del__(self):
        print("Inside (Destructor):")

def main():
        print("Inside main")
        obj = Demo()
        print("Inside Demo:", obj)

    
if __name__ == "__main__":
    main()
    print("End of application")