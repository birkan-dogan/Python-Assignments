"""
Imagine you have a list of strings.

liste = ["345","sadas","324a","14","kemal"]

Print the strings in this list that contain only numbers to the screen. Remember to use try,except blocks when doing this.

"""
liste = ["345","veli","324a","14","ali"]

for i in liste:
  try:
    answer = int(i)
    print(answer)

  except ValueError:
    print("this is not only a numeric type")
