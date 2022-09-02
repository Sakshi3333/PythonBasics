from sys import*

def main():
    print("Number of commandline arguements are:", len(argv))
    print("Name of application:", argv[0])
    print("First argument:",argv[1])
    print("Second argument:", argv[2])

if __name__ == "__main__":
    main()