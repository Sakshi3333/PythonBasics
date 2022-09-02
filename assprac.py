
def main():
    print("Enter the name of file that you want:")
    name = input()
    fd = open(name,'rb')
    data = fd.read()
    fd.seek()
    data = fd.read()
    print(data)

if __name__ =="__main__":
    main()