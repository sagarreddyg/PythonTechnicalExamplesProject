def getnum():
    try:
        num = int(input("Please enter your number to find square root : "))
    except ValueError:
        print("Please enter Numbers only ")
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
