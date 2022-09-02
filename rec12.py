i = 0  
def fun(i=0):
       # LOCAL VARIABLE
       if (i < 5):
        print (i)
        i = i + 1
        fun(i)
def main():
    fun()
 

if __name__ == "__main__":
    main()