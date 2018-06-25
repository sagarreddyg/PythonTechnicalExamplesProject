def getnum():
    try:
        num = int(input("Please enter your number to find square root : "))
        if num <= 0:
            print("Please enter positive number and other than zero")
            num = getnum()
    except ValueError:
        print("Please enter valid input")
        getnum()
    else:
        return num


def main():
    a = getnum()
    res = a ** 0.5
    print("Square of a given number is : ", res)


if __name__ == "__main__":
    main()
    input()
