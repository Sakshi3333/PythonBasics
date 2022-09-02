import sys
def DisplayR(no):
    print(no)
    no = no + 1
    DisplayR(no)
  

def main():
    DisplayR(0)
    no = sys.getrecursionlimit()
    print(no)

if __name__ == "__main__":
    main()