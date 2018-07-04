
def gettinginput1():
    num1 = int(input("Please enter your starting range Positive and other than Zero to printing Odd number's : "))
    while num1 <= 0:
        num1 = gettinginput1()
    else:
        return num1


def gettinginput2():
    num2 = int(input("Please enter your  ending range more than starting To printing Odd number's : "))
    while num2 <= 0:
        num2 = gettinginput2()
    else:
        return num2


def inputfromuser():
    try:
        num01 = gettinginput1()
        num02 = gettinginput2()
        while num01 > num02:
            num02 = gettinginput2()
        while num01 == num02:
            num02 = gettinginput2()

    except ValueError:
       print("Enter only Integer values")
       inputfromuser()
    else:
       coun = 0
       for i in range(num01, num02 + 1):
           if i % 2 != 0:
               print(i, end=" ")
               coun += 1
       print("\nTotal number of Odd numbers between {} to {} is {}".format(num01, num02, coun))


inputfromuser()
input()
