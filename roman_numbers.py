# Purpose of the this coding challenge is to write a code for converting to Roman Numerals. 

dict1 = {"I" : 1, "IV":4 ,"V" : 5, "IX":9 ,"X":10, "XL":40 ,"L": 50, "XC": 90 ,
         "C": 100, "CD":400 ,"D": 500, "CM": 900 ,"M": 1000}  
          # we have breakpoints for some numbers to convert it to roman numbers. Instance, 4 or 9. 
          # we cannot access them with the roman numbers' rules, so we should have their values.

prompt = int(input("integer: ")) 

index = 12
roman = ""

while prompt:

  if prompt >= list(dict1.values())[index]:
    prompt = prompt - list(dict1.values())[index]
    roman += list(dict1.keys())[index]
  else:
    index -= 1
print(roman)
