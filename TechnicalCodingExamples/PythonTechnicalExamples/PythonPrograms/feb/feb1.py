a, b = 0, 1
for i in range(100):
  if a <= 100:
    print(a, end=" ")
    a, b = b, a
    b += a
