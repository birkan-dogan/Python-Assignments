# A comfortable word is a word which you can type always alternating the hand you type 
# with (assuming you type using a Q-keyboard and use of the ten-fingers standard).
# The word will always be a string consisting of only letters from a to z.
# Write a program which returns True if it's a comfortable word or False otherwise.


word = input("bir kelime giriniz:")
word = set(word.lower())
Left = {"q", "w", "e", "r", "t", "a", "s", "d", "f", "g", "z", "x", "c", "v", "b"}
right = {"y", "u", "i", "o", "p", "h", "j", "k", "l", "n", "m", "ı", "ğ", "ü", "ş", "ö", "ç"}
a = word.intersection(right)
b = word.intersection(Left)
print(bool(a and b))
