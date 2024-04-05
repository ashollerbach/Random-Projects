def fib(n):
  a = 1
  b = 0
  holder = 1
  for i in range(n):
    holder = a
    a = a + b
    b = holder
  print(a)

for j in range(100):
  fib(j)