# "paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．

import nltk

word1 = "paraparaparadise"
word2 = "paragraph"
X = []
Y = []

bigram1 = nltk.ngrams(word1, 2)
bigram2 = nltk.ngrams(word2, 2)


def bigram_x(x):
  for b1 in bigram1:
    x.append(b1)
  return x

def bigram_y(y):
  for b2 in bigram2:
    y.append(b2)
  return y

bigram_x(X)
bigram_y(Y)

X1 = set(X) #集合は辞書型にしなければならない
Y1 = set(Y)

print('X:{}'.format(X1))
print('Y:{}'.format(Y1))
print('和集合:{}'.format(X1 | Y1))
print('積集合:{}'.format(X1 & Y1))
print('差集合:{}'.format(X1 ^ Y1))

# {1, 3} <= {1, 2, 3}
print('seがXに含まれる:{}'.format({('s', 'e')} <= X1))
print('seがYに含まれる:{}'.format({('s', 'e')} <= Y1))


