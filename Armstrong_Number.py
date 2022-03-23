while True :

  number = input("enter a positive integer number: ")
  digits = len(number)
  summ = 0

  if not number.isdigit() :

    print(number, "is invalid entry. please enter valid input.")

  else:

    for i in range(digits) :

      summ += int(number[i]) ** digits
    if summ == int(number):
      print(number, "is an armstrong number.")
      break
    else:
      print(number, "not armstrong")
      break
