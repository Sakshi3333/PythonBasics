from sys import*

def main():
    print("Number of command line arguments are:", len(argv))
    print("Name of application is:", argv[0])
   
   
    ans = int(argv[1]) + int(argv[2])
   
    print ("Additions is :",ans )

for data in argv:
    print(data)

if __name__ =="__main__":
    main()