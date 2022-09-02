def main():
    print("Enter the file name you want to create")
    name=input()

    fd = open(name,"w")
    print("Enter the data that you want to write in the file")
    data=input()
    fd.write(data)
    fd.close()

if __name__ =="__main__":
    main()