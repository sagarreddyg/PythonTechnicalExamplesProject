# Additionofmatrix.py
row = int(input("Please enter your row values : "))
col = int(input("Please enter your column value : "))
a = []
X = []
Y = []
R = []
for i in range(row):
    for j in range(col):
        a.append(int(input("Please enter your {} value of {} Row".format(j, i))))
    X.append(a)
    a = []
for i in range(row):
    for j in range(col):
        a.append(int(input("Please enter your {} value of {} Row".format(j, i))))
    Y.append(a)
    a = []

# iterate through rows
for i in range(len(X)):
    for j in range(len(X[0])):# iterate through columns
        a.append(X[i][j] + Y[i][j])
    R.append(a)
    a = []
for r in R:
    print(r)

