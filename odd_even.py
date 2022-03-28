"""
Write a function that queries whether a number is even. This function returns this value with return if the number is even.
However, if the number is odd, the function raise will throw a ValueError.
Next, define a list that contains even and odd numbers, and scroll through the list to print only even numbers to the screen.
"""

def odd_even(parametre):

  if parametre % 2 == 0:
    return parametre

  else:
    raise ValueError("it is not even number")


list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # the list for this question

for i in list1:
  try:
    print(odd_even(i))
  except ValueError:
    pass
