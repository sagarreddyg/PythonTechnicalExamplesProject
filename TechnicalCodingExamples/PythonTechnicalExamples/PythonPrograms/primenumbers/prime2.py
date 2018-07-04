num1 = int(input("Please enter your number :"))
count = 0
for j in range(2, num1):
  if num1 % j == 0:
    count += 1
if count == 0:
  print(num1,"is a prime number.")
else:
  print(num1,"is not a prime number.")