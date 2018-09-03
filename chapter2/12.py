# 12. 1列目をcol1.txtに，2列目をcol2.txtに保存
# 各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．確認にはcutコマンドを用いよ．

import numpy as np

document = open('hightemp.txt')

def tab_space(document):
  d_list = ''
  for doc in document:
    d = doc.expandtabs(1)
    d_list += d
  return d_list

doc_list = tab_space(document)
print(doc_list)


# def split_row():

