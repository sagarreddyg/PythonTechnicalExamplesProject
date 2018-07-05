col = int(input("Please enter your column value : "))
row = int(input("Please enter your row values : "))

a = []
X = []
y = []
for i in range(row):
    for j in range(col):
        a.append(int(input("Please enter your {} value of {} Row".format(j, i))))
    X.append(a)
    a = []
print(X)

