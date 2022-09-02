import os

def main():
    print("Enter the file name you want to create")
    name=input()

    if os.path.exists(name):
      os.remove(name)
      print("File gets deleted")
    

if __name__ =="__main__":
    main()