def DisplayR(no):
    if (no > 0):
       print("SHREE GURUDEV DATTA")
       no = no - 1
       DisplayR(no)

def main():
    DisplayR(3)

if __name__ == "__main__":
    main()