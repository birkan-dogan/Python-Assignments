"""
Verilen oyun için sudoku doğru çözüldüyse true, doğru çözülmediyse false döndürün.
Sudoku oyun alanı 9 tane 3 x 3 küçük dizeyden (matrix) oluşan 9 x 9'luk büyük bir dizeyden oluşur.
Büyük dizeyin her satır ve sütunuyla birlikte küçük dizeylerin her birine 1'den 9'a kadar olan tüm rakamlar 
her rakam tek bir kez kullanılarak yerleştirildiğinde oyun çözülmüş olur.

[[9, 1, 6, 2, 5, 8, 3, 7, 4], 
[7, 3, 8, 1, 4, 9, 6, 2, 5], 
[4, 5, 2, 6, 7, 3, 8, 1, 9], 
[1, 7, 4, 8, 2, 5, 9, 3, 6], 
[6, 2, 9, 4, 3, 1, 7, 5, 8], 
[5, 8, 3, 7, 9, 6, 2, 4, 1], 
[3, 6, 7, 9, 1, 4, 5, 8, 2], 
[8, 4, 5, 3, 6, 2, 1, 9, 7], 
[2, 9, 1, 5, 8, 7, 4, 6, 3]]  --->  Output: True

[[9, 1, 6, 2, 5, 8, 3, 7, 4], 
[9, 3, 8, 1, 4, 9, 6, 2, 5], 
[4, 5, 2, 6, 7, 3, 8, 1, 9], 
[1, 7, 4, 8, 2, 5, 9, 3, 6], 
[6, 2, 9, 4, 3, 1, 7, 5, 8], 
[5, 8, 3, 7, 9, 6, 2, 4, 1], 
[3, 6, 7, 9, 1, 4, 5, 8, 2], 
[8, 4, 5, 3, 6, 2, 1, 9, 7], 
[2, 9, 1, 5, 8, 7, 4, 6, 3]] ---> Output: False

"""

oyun = [[1, 7, 6, 2, 3, 9, 4, 5, 8], 
        [5, 2, 4, 7, 8, 1, 3, 6, 9], 
        [3, 8, 9, 5, 6, 4, 1, 7, 2], 
        [6, 4, 1, 3, 9, 2, 7, 8, 5], 
        [7, 5, 8, 1, 4, 6, 9, 2, 3], 
        [2, 9, 8, 8, 7, 5, 6, 4, 1], 
        [9, 1, 7, 4, 2, 8, 5, 3, 6], 
        [4, 6, 2, 9, 5, 3, 8, 1, 7], 
        [8, 3, 5, 6, 1, 7, 2, 9, 4]]    # False çıktısı vermeli

dict1 = {}

a = 0
b = 0
c = 0
for i in oyun:

  while set(range(1,10)) == set(i) : 
      if a == 9 :  # a == 9 olduğunda sıfırlamazsak list: out of range hatası alırız
        a = 0
        c += 1   # her oyunumuzda a değişkeni 9 kere sıfırlanmalı. c == 9 olduğunda oyun bitmeli.

      if i[a] not in dict1:  # i[0] olarak düşünülmeli

        dict1[i[a]] = 1
        a += 1

      else:
        dict1[i[a]] += 1 
        a += 1

      if c == 9:
        break

for i in dict1.values():
  b += i

if b != 90:
  print(False)
else:
  print(True)
