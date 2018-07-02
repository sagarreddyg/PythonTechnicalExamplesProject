def gethelloworld():
    a = str(input("Please Hello World! Only : "))
    while a != "Hello World!":
        gethelloworld()
    else:
        return a


s = gethelloworld()
print(s)
