def outer():
    print("Inside outer function")

    def inner():
       print("Inside inner function")

    inner()             # CALL
def main():
    outer()


if __name__ == "__main__":
    main()