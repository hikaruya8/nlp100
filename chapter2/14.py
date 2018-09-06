# 14. 先頭からN行を出力
# 自然数Nをコマンドライン引数などの手段で受け取り，入力のうち先頭のN行だけを表示せよ．確認にはheadコマンドを用いよ．


import nltk
import numpy as np #numpyで2次元配列にする

def make_col_n(n):
  f = open('hightemp.txt')
  document = f.read()
  doc_token = nltk.word_tokenize(document)
  doc_2d = np.array(doc_token).reshape((24,4)) #24行4列 ndarrayにする

  row_n = doc_2d[int(n),:] #1~n行目を抜き出したもの


  path_w = '/Users/yamadahikaru/Projects/ML_Projects_Python/nlp100/chapter2/row_n.txt'

  l = row_n

  with open(path_w, mode='w') as f:
    f.write(' '.join(l))

  with open(path_w) as f:
    print(f.read())

n = input("自然数(半角数字)を入力してください: ")
make_col_n(n)