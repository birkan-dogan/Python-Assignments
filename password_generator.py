# password generator
"""
we will use random module and its methods for creating a new password.

random.randint(a, b)  --> it returns integer in range[a, b]
random.shuffle(list_name)  --> it shuffle list x in place, and return None

chr() ---> build-in function, convert ASCII to str
"""

# we want to make a password and password has 3 upper-case, 3 lower-case, 3 number and 2 special character

import random

uppers = [chr(random.randint(65, 90)) for i in range(3)]  # will have random strs between A-Z in a list

lowers = [chr(random.randint(97, 122)) for i in range(3)]  # will have random strs between a-z in a list

numbers = [chr(random.randint(48, 57)) for i in range(3)]  # will have random strs between 0-9 in a list

chars = chr(random.randint(33, 47)) + chr(random.randint(58, 64))  # will have random strs special characters in a str

passw = uppers + lowers + numbers + list(chars)

random.shuffle(passw)

"""
we can also define a function for shuffling

def shuffling(password):
  templist = list(password)
  random.shuffle(templist)
  return "".join(templist)

"""
print("".join(passw))
