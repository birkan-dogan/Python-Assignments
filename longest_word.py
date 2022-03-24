# find and print the length of the longest word.
# take a string sentence from the user(consisting of a couple of words)
# compares and find out the longest word as int type


sentence = input("Give me a sentence: ")
word_list = sentence.split()
longest = 0
i = 0
while i < len(word_list):
  if len(word_list[i]) > longest:
    longest = len(word_list[i])
  i += 1
print("The length of the longest word: ", longest)
