"""
how can be reached the target number  by adding which two elements of the list of integers

ex.)
sayılar = [3, 2, 7]
target = 10

output: [0, 2]  ---> because sayılar[0] + sayılar[2] = 10
"""

sayılar = [3, -4, 2, 8, 11]
target = 5
a = 0
b = []

for i in sayılar:

  if (target - i) in sayılar:

    b.append(a)
    a += 1  # it is counting for index number

  else:
    a += 1  # it is counting for index number

print(b)
