"""
input    output

"()"     True
"()[]{}" True
"(]"     False
"([)])"  False
"({[]})" True
""       True


in any case, there is an open and close parenthesis in the innermost part.
Therefore, if we go from the inside by deleting, 
we should not have any parentheses for it to be True.
"""

def isValid(s):

  while "()" in s or "{}" in s or "[]" in s:   # we just want the loop to run continuously
    s = s.replace("()", "").replace("[]", "").replace("{}", "")  #  .replace() method returns a string
  return s == ""


# for example

isValid("[(){([])}]([{}])")  # it should return True because it is valid
