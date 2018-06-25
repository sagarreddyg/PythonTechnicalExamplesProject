def Print1():
    result_str = ""
    for row in range(7):
        for col in range(7):
            if (col == 3)or (row == 1 and 1 < col < 3) or (row == 2 and col == 1) or (row == 6 and 1 <= col <= 5):
                result_str = result_str + "* "
            else:
                result_str = result_str + "  "
        result_str = result_str + "\n"
    print(result_str)


def Print2():
    result_str = ""
    for row in range(0, 7):
        for column in range(0, 7):
            if (((column == 0 or column == 4) and (1 <= row < 3)) or (row == 3 and column == 3)or (row == 4 and column == 2)or (row == 5 and column == 1)or (((row == 0 and column <=3) or (row == 6)) and (0 < column < 5))):
                result_str = result_str + "* "
            else:
                result_str = result_str + "  "
        result_str = result_str + "\n"
    print(result_str)


def Print3():
    result_str = ""
    for row in range(0, 7):
        for column in range(0, 7):
            if (((column == 5) and (row >= 1 and row != 6)and (row != 3)) or ((row == 0 or row == 6)or (row == 3 and column >= 3)) and ((0 != column < 5))):
                result_str = result_str + "* "
            else:
                result_str = result_str + "  "
        result_str = result_str + "\n"
    print(result_str)


def Print4():
    result_str = ""
    for row in range(0, 7):
        for column in range(0, 7):
            if (column == 0 or row == 4)and(row <= 4) or (row == 2 and column == 3)or (row == 3 and column == 3)or (row == 5 and column == 3)or (row == 6 and column == 3):
                result_str = result_str + "* "
            else:
                result_str = result_str + "  "
        result_str = result_str + "\n"
    print(result_str)


def Print5():
    result_str = ""
    for row in range(0, 7):
        for column in range(0, 7):
            if (((column == 5) and (row <= 4)and(row >= 3)) or(row <= 3 and column == 1)or ((row == 0 or (row == 5 and (1<column < 5)))or(row == 2 and column < 5)) and ((0 != column < 6 ))):
                result_str = result_str + "* "
            else:
                result_str = result_str + "  "
        result_str = result_str + "\n"
    print(result_str)


def Print6():
    result_str = ""
    for row in range(0, 7):
        for column in range(0, 7):
            if ((((column == 0 and (row != 0 and row != 1)) or column == 4) and (row != 6)and (row >= 4 or column == 0)) or (row==1 and column == 4)or ((row == 6)or (row == 3 and column >= 2) or(row == 0 and column == 2)or (row == 0 and column == 3) or ((row == 1 or row == 4) and column == 1)) and ((0 != column < 4))):
                result_str = result_str + "* "
            else:
                result_str = result_str + "  "
        result_str = result_str + "\n"
    print(result_str)


def Print7():
    result_str = ""
    for row in range(0, 7):
        for column in range(0, 7):
            if (row == 0) or (row == 1 and column == 6) or (row == 2 and column == 5) or (row == 3 and column == 4)or (row == 4 and column == 3)or (row == 5 and column == 2):
                result_str = result_str + "* "
            else:
                result_str = result_str + "  "
        result_str = result_str + "\n"
    print(result_str)


def Print8():
    result_str = ""
    for row in range(0, 7):
        for column in range(0, 7):
            if (((column == 0 or column == 6) and (row >= 1 and row != 6) and (row != 3)) or (
                    ((row == 0 or row == 6) or row == 3) and (0 < column < 6))):
                result_str = result_str + "* "
            else:
                result_str = result_str + "  "
        result_str = result_str + "\n"
    print(result_str)


def Print9():
    result_str = ""
    for row in range(0, 7):
        for column in range(0, 7):
            if ((((column == 0 and row <= 2) or (column == 5 and row <= 3)) and (row >= 1)) or(row == 4 and column == 4)or(row == 5 and column == 3) or(row == 6 and column == 2)or (((row == 0 and column != 5) or row == 3) and (0 < column < 6))):
                result_str = result_str + "* "
            else:
                result_str = result_str + "  "
        result_str = result_str + "\n"
    print(result_str)


def Print0():
    result_str = ""
    for row in range(0, 7):
        for column in range(0, 7):
            if (((column == 0 or column == 6) and (row >= 2 and row <= 4))or((row == 1 or row == 5) and column == 1)or((row == 1 or row == 5) and column == 5) or (((row == 0 or row == 6)) and (1 < column < 5))):
                result_str = result_str + "* "
            else:
                result_str = result_str + "  "
        result_str = result_str + "\n"
    print(result_str)
