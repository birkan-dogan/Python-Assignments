# write a program to count the elements and create a dict to show the count

liste = [11, 45, 8, 11, 23, 45, 23, 45, 89]
dict1 = {}
for i in liste:
  if i not in dict1:
    dict1[i] = 1
  else:
    dict1[i] += 1
print(dict1)
