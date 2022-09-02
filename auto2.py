from sys import*

def Addition():
    Ans = int(argv[1]) + int(argv[2])
# ENTRY POINT OF AUTOMATION SCRIPT
def main():
    print("----------- SHREE GANESHAYA NAMAH -------------------------")
    print("Script name:", argv[0])
    print("Number of arguments accepted:", len(argv[0]))

    if (len(argv) > 3) or (len(argv) < 2):
        print("Invalid number of arguments")
        exit()
    if(len(argv= [2])):
     if (argv[1] =="-u") or (argv[1] == "-U"):
        print("Usage: Script is used to perform addition of 2 numbers")
        
        exit()

    if (argv[1] == "-h") or (argv[1] == "-H"):
        print("Help:Name_of_Script First_Argument Second_argument")
        print("First_Argument: any numeric value")
        print("Second_Argument: any numeric value")
        exit()

    iRet = Addition(int(argv[1])), (int(argv[2]))
    print("Addition is:",iRet)

# STARTER OF THE AUTOMATION SCRIPT
if __name__ =="__main__":
 main()