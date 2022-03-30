# comparing the answer key with the student's answers. Just use the map() function.
answer_key = ["a", "c", "e", "b", "a"]
student_1 = ["a", "d", "d", "b", "a"]

result = map(lambda x, y : "True" if x == y else "False", answer_key, student_1)

"""
map(function, iterables)

map() function, hover over the given iterables with the function inside.

"""

