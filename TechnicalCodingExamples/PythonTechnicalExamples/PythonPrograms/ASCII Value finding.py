def getinput():
    ch = str(input("Please enter your character to find ASCII Value : "))
    return ch
def finding():
    try:
        nm = getinput()
        if nm == None:
            finding()
    except ValueError:
        print("Please enter only char values")
        finding()
    else:
        print("ASCII Value of given Character's is:",end="")
        for i in range(len(nm)):
            print(ord(nm[i]),end=",")
finding()
input()
