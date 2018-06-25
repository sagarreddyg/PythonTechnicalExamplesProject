def getinput():
    try:
        side1 = int(input("Please enter your value for side 1 : "))
        side2 = int(input("Please enter your value for side 2 : "))
        side3 = int(input("Please enter your value for side 3 : "))
    except ValueError:
        print("Please enter Positive values and other than zero")
        getinput()
    else:
        return side1, side2, side3
def calarea():
    a, b, c, = getinput()
    s = (a+b+c)/2
    res = s*(s - a)*(s - b)*(s - c)
    return res ** 0.5
def main():
    print(calarea())
if __name__ == "__main__":
    main()
    input()
