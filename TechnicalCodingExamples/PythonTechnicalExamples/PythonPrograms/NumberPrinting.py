import PrintingNumbersStarFormat as NP

inp = input("Please enter your Number : ")
for i in range(len(inp)):
    if int(inp[i]) == 0:
        NP.Print0()
    elif int(inp[i]) == 1:
        NP.Print1()
    elif int(inp[i]) == 2:
        NP.Print2()
    elif int(inp[i]) == 3:
        NP.Print3()
    elif int(inp[i]) == 4:
        NP.Print4()
    elif int(inp[i]) == 5:
        NP.Print5()
    elif int(inp[i]) == 6:
        NP.Print6()
    elif int(inp[i]) == 7:
        NP.Print7()
    elif int(inp[i]) == 8:
        NP.Print8()
    elif int(inp[i]) == 9:
        NP.Print9()
