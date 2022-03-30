"""
take the age of the user using input() and while loop
write a program that, 1.)takes the age from the user
and check the age if it is correct numeric format
"""

age = input("enter your age: ")

while age.isdigit() == False:
  print("you entered incorrectly!")
  age = input("enter your age please: ")

print("Great! You entered valid input!")
