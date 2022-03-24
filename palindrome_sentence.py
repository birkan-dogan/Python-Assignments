def palindrom(a):

  '''
  palindrome is a word, phrase, or sequence that reads the same backwards as forwards, e.g. madam or nurses run.
  '''

  b = ""

  for i in a.lower():
    if i.isalnum():
      b += i

  if b == b[::-1]:
    print(a, "is a palindrome")

  else:
    print(a, "is not a palindrome")

