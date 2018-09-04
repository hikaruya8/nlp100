# 12. 1列目をcol1.txtに，2列目をcol2.txtに保存
# 各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．確認にはcutコマンドを用いよ．

import nltk
import numpy as np #numpyで2次元配列にする

f = open('hightemp.txt')
document = f.read()
doc_token = nltk.word_tokenize(document)
doc_2d = np.array(doc_token).reshape((24,4)) #24行4列 ndarrayにする

col1_txt = doc_2d[:,0] #各行の1列目だけを抜き出したもの
col2_txt = doc_2d[:,1] #各行の1列目だけを抜き出したもの


path_w = '/Users/yamadahikaru/Projects/ML_Projects_Python/nlp100/chapter2/12.py'
s = 'col1_txt'

with open(path_w, mode='w') as f:
    f.write(s)
with open(path_w) as f:
    print(f.read())

# New file

# print(f)
# print(col2_txt)
# def split_row(document):
#   d_list = []
#   for d in document:
#     d_list += d
#   return d_list


# print(split_row(document))




