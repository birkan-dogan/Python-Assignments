# we are using List Comprehension
"""
The syntax ----> [expression for item in iterable]

if we have conditional statements
The syntax ----> [expression for item in iterable if condition]
"""

# what will be the output of the code?

a = [1, 2, 3, 4]
b = [sum(a[0: x + 1]) for x in range(0, len(a))]

"""
the solution will be step by step
[sum(a[0: x + 1]) for x in range(0, 4)]
[sum(a[0: x + 1]) for x in 0, 1, 2, 3]
[sum(a[0: 1]) for x in 0, 1, 2, 3]  # 1
[sum(a[0: 2]) for x in 0, 1, 2, 3]  # 1 + 2
[sum(a[0: 3]) for x in 0, 1, 2, 3]  # 1 + 2 + 3
[sum(a[0: 4]) for x in 0, 1, 2, 3]  # 1 + 2 + 3 + 4
and we know that list comprehension returns a list. 
"""
print(b)
