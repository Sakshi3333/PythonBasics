import os

def main():
    print("Enter the file name you want to create")
    name=input()

    if os.path.exists(name):
      fd = open(name,"r")
      print(type(fd))
    
    data=fd.read(5)
    print("Data from file:", data)
    fd.close()

if __name__ =="__main__":
    main()