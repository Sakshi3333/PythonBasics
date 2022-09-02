from sys import*
#def fun():
  
def main():
     print("Shree ganeshaya namah")
     print("Automation scripts")
     print("Application name:", +argv[0])

if (len(argv)!=3):
        print("ERROR:Invalid number of arguments")
        exit()

if argv[1]=='-h':
        print("The script is designed for_________________________")
        exit()

if argv[1]=='-u':
        print("Usage:Application_name ______________________")

try:
        fun(argv[1])
except Exception as E:
        print("ERROR:Invalid input" +E)

if((len(argv)< 1 )or (len(argv)> 3)):
        print("Error:Invalid number of arguments")

if __name__ =="__main__":
    main()