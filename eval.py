"""
In python we have eval() built-in function.
This function acts to strings like they are not a string.
ex.) eval("15+7") returns 22
     eval("18*2") returns 36

and I want to build my own eval() function and its name is evaluate()

"""
def evaluate(a):

  liste = ["+", "-", "/", "*"]
  for i in a:

    if i in liste:
      nmbr1 = a[:a.index(i)]
      nmbr2 = a[a.index(i) + 1:]

      if i == "+":
        return int(nmbr1) + int(nmbr2)
      elif i == "-":
        return int(nmbr1) - int(nmbr2)
      elif i == "*":
        return int(nmbr1) * int(nmbr2)
      else:
        return int(nmbr1) / int(nmbr2)
