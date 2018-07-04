num1 = int(input("Please enter your range to print prime numbers : "))
for i in range(2, num1 + 1):
  count = 0
  for j in range(2, i):
    if i % j == 0:
      count += 1
  if count == 0:
    print(i, end=" ")