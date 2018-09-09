# 18. 各行を3コラム目の数値の降順にソート
# 各行を3コラム目の数値の逆順で整列せよ（注意: 各行の内容は変更せずに並び替えよ）．確認にはsortコマンドを用いよ（この問題はコマンドで実行した時の結果と合わなくてもよい）．

import nltk
import numpy as np #numpyで2次元配列にする

def sort_row3():
  f = open('hightemp.txt')
  document = f.read()
  doc_token = nltk.word_tokenize(document)
  doc_2d = np.array(doc_token).reshape((24,4)) #24行4列 ndarrayにする
  print(doc_2d[:, doc_2d[2].argsort(axis=0, kind='quicksort')][::-1])

sort_row3()