def outer():           # 0X100
    print("Inside outer function")

    def inner():       # 0X200
       print("Inside inner function")

    return inner        #0X200
    
def main():
    func_name = outer()    # ITS CALL TO OUTER FUNCTION
    func_name()           # ITS CALL TO INNER FUNCTION


if __name__ == "__main__":
    main()