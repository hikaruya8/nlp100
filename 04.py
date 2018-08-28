import nltk

elements = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
words = nltk.word_tokenize(elements) #単語分割
num_first_only = (1, 5, 6, 7, 8, 9, 15, 16, 19)
result = {}

for num, words in enumerate(words):
  if num == num_first_only:
    result[words[0:1]] = num
  else:
    result[words[0:2]] = num

print(result)

