import AlphabetPrinting as al


def getname():
    name = input("Please enter your name : ")
    return name


def printname():
    n = getname()
    for i in range(len(n)):
        if n[i] == "A":
            al.printa()
        elif n[i] == "B":
            al.printb()
        elif n[i] == "C":
            al.printc()
        elif n[i] == "D":
            al.printd()
        elif n[i] == "E":
            al.printe()
        elif n[i] == "F":
            al.printf()
        elif n[i] == "G":
            al.printg()
        elif n[i] == "H":
            al.printh()
        elif n[i] == "I":
            al.printi()
        elif n[i] == "J":
            al.printj()
        elif n[i] == "K":
            al.printk()
        elif n[i] == "L":
            al.printl()
        elif n[i] == "M":
            al.printm()
        elif n[i] == "N":
            al.printn()
        elif n[i] == "O":
            al.printo()
        elif n[i] == "P":
            al.printp()
        elif n[i] == "Q":
            al.printq()
        elif n[i] == "R":
            al.printr()
        elif n[i] == "S":
            al.prints()
        elif n[i] == "T":
            al.printt()
        elif n[i] == "U":
            al.printu()
        elif n[i] == "V":
            al.printv()
        elif n[i] == "W":
            al.printw()
        elif n[i] == "X":
            al.printx()
        elif n[i] == "Y":
            al.printy()
        elif n[i] == "Z":
            al.printz()


def main():
    printname()
    input()


if __name__ == "__main__":
    main()
