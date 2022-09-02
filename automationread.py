def main():
    print("Enter the file name you want to create")
    name=input()

    fd = open(name,"r")
    
    data=fd.read(5)
    print("Data from file:", data)
    fd.close()

if __name__ =="__main__":
    main()