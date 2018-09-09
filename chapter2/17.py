# 17. １列目の文字列の異なり
# 1列目の文字列の種類（異なる文字列の集合）を求めよ．確認にはsort, uniqコマンドを用いよ．

import nltk
import numpy as np #numpyで2次元配列にする

def diff_str():
  f = open('hightemp.txt')
  document = f.read()
  doc_token = nltk.word_tokenize(document)
  doc_2d = np.array(doc_token).reshape((24,4)) #24行4列 ndarrayにする

  row1 = doc_2d[:,0]
  
  for r in row1:
    if r.isnumeric() == True:
      print("数字")
    elif r.isalpha() == True:
      print("英字or日本語")
    elif r.isalnum() == True:
      print("英数字")

  # path_w = '/Users/yamadahikaru/Projects/ML_Projects_Python/nlp100/chapter2/17.txt'

  # for l in doc_2d:
  #   with open(path_w, mode='w') as f:
  #     f.write(' '.join(l))
  #   with open(path_w) as f:
  #     print(f.read())


diff_str()