# create a python set such that it shows the element from both lists in a pair

first_list = [2, 3, 4, 5, 6, 7, 8]
second_list = [64, 4, 9, 25, 16, 36, 49]

set1 = set()  # we should have set because of unrepetable

for i in first_list:

  if i ** 2 in second_list:  # in this case, we are looking at both lists
    a = i, i ** 2
    set1.add(a)   # and we are using set.add() method to add new item to the set

print(set1)
