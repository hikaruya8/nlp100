# "paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．

import nltk

word1 = "paraparaparadise"
word2 = "paragraph"
X = []
Y = []

bigram1 = nltk.ngrams(word1, 2)
bigram2 = nltk.ngrams(word2, 2)
def bi_gram(x, y):
  for b1, b2 in zip(bigram1, bigram2):
    x.append(b1)
    y.append(b2)
  return x, y

bi_gram(X, Y)

print('和集合:{}'.format(X | Y))



