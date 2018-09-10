# 19. 各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べる
# 各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．確認にはcut, uniq, sortコマンドを用いよ．

from collections import Counter
import numpy as np
import nltk

def count_row1():
  f = open('hightemp.txt')
  document = f.read()
  doc_token = nltk.word_tokenize(document)
  doc_2d = np.array(doc_token).reshape((24,4)) #24行4列 ndarrayにする

  unique, counts = np.unique(doc_2d[0:, 0], return_counts=True)
  print(np.asarray((unique, counts)).T)

  # doc_list2d = doc_2d.tolist()
  # for d in doc_list2d:
  #   counter = Counter(d[0])

    # print(counter)

count_row1()