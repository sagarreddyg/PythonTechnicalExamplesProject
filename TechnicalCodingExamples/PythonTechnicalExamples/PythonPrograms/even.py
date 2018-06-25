def gettinginput1():
    num1 = int(input("enter your range from printing Even number's : "))
    while num1 <= 0:
        print("Please enter number Positive and other than Zero ")
        num1 = gettinginput1()
    else:
        return num1
def gettinginput2():
    num2 = int(input("enter your range To printing Even number's : "))
    while num2 <= 0:
        print("Please enter number Positive and other than Zero ")
        num2 = gettinginput2()
    else:
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
       for i in range(num01, num02 + 1):
           if i % 2 == 0:
               print(i, end=" ")
               coun += 1
       print("\nTotal number of Even numbers between {} to {} is {}".format(num01, num02, coun))
inputfromuser()
input()
