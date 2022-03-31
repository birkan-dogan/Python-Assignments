# build a calculator using with lambda expression

"""
ex.)
      calculator["+"](4, 5)  ----> 9
the question has to be asked, can a lambda expression be value of any dictionary?
"""

calculator = {"+" : (lambda x, y: x + y),
              "-" : (lambda x, y: x - y),
              "*" : (lambda x, y: x * y),
              "/" : (lambda x, y: x / y)}


calculator["*"](8, 5)  # it works
