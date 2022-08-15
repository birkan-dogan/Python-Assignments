# input all is well --> output AIW
# write a program and it makes words acronyms

user_input = str(input("Enter a Phrase: "))

text = user_input.split()
# print(text)

acronyms = ""

for i in text:
  acronyms += str(i[0]).upper()

print(acronyms)  
