import os
def main():
    print("Enter the file name you want to create")
    name=input()

    fd = open(name,"rb")
    data = fd.read(5)
    
    fd.seek(3,1)
    
    data = fd.read()
    print(data)

if __name__ =="__main__":
    main()