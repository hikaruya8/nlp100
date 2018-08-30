# 与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．
import nltk
words_bi = []
char_bi = []

def ngram(words, n):
  tokens = nltk.word_tokenize(words)
  bigram = nltk.ngrams(tokens, n)
  for bi in bigram:
    words_bi.append(bi)
    for b in bi:
      char = nltk.ngrams(b, n)
      for c in char:
        char_bi.append(c)
  return words_bi, char_bi

words = "I am an NLPer"
print(ngram(words, 2))
