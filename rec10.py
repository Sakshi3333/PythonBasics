i = 0  
def fun():
       global i    # LOCAL VARIABLE
       if (i < 5):
        print (i)
        i = i + 1
        fun()
def main():
    fun()
 

if __name__ == "__main__":
    main()