# 12. 1列目をcol1.txtに，2列目をcol2.txtに保存
# 各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．確認にはcutコマンドを用いよ．

import nltk
import numpy as np #numpyで2次元配列にする

f = open('hightemp.txt')
document = f.read()
doc_token = nltk.word_tokenize(document)
doc_2d = np.array(doc_token).reshape((24,4))
print(doc_2d)

# def tab_space(document):
#   d_list = ''
#   for doc in document:
#     d = doc.expandtabs(1)
#     d_list += d
#   return d_list

# def split_row(document):
#   d_list = []
#   for d in document:
#     d_list += d
#   return d_list


# print(split_row(document))




