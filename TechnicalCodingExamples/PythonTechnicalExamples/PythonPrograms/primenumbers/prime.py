def getinput1():
    num1 = int(input("Please enter the range more than one to get PrimeNumbers : "))
    if num1 <= (0 or 1):
        num1 = getinput1()
    return num1


def getoutput():
    try:
        num1 = getinput1()
    except ValueError:
        print("Please enter onely integer values ")
        getoutput()
    else:
        print("Prime Numbers are : ", end="")
        for i in range(2, num1 + 1):
            count = 0
            for j in range(2, i):
                if i % j == 0:
                    count += 1
            if count == 0:
                print(i, end=" ")
getoutput()
input()
