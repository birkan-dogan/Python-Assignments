# create a list consisting of Fibonacci numbers from 1 to 55 using control flow
# statements and range() function.

fibo = [1, 1]  # Fibonacci number system starts with 1, 1
               # the question wants us to create a list in 10 elements.
               # and we just need 8 another number to complete the task.

for i in range(8):
  fibo.append(fibo[-1] + fibo[-2])

print(fibo)


fibo2 = [1, 1]
for i in range(10):
  fibo2.append(fibo2[-1]+ fibo2[-2])

print(fibo2)
