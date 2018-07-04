# even.py
def gettinginput1():
    num1 = int(input("Please enter starting range : "))
    return num1


def gettinginput2():
    num2 = int(input("Please enter ending range more than starting range : "))
    return num2


def inputfromuser():
    try:
        num01 = gettinginput1()
        num02 = gettinginput2()
        while num01 > num02:
            print("Enter Valid input num1 is smaller than num2")
            num02 = gettinginput2()
        while num01 == num02:
            print("Please enter different number's")
            num01 = gettinginput1()
            num02 = gettinginput2()

    except ValueError:
       print("Enter only Integer values")
       inputfromuser()
    else:
       coun = 0
       print("Even numbers: ", end="")
       for i in range(num01, num02 + 1):
           if i % 2 == 0:
               print(i, end=" ")
               coun += 1
       print("\nTotal number of Even numbers between {} to {} is {}".format(num01, num02, coun))


inputfromuser()
input()
