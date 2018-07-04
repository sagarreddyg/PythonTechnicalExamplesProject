# Square root of a number with out any exception
def getnum():
    num = float(input("Please enter your number to find square root : "))
    return num


def main():
    try:
        a = getnum()
    except ValueError:
        print("Please enter Numbers Only")
        main()
    else:
        res = a ** 0.5
        print("Square of a given number is : ", res)


if __name__ == "__main__":
    main()
    input()
