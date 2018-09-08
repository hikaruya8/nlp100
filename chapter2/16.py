# 16. ファイルをN分割する
# 自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．同様の処理をsplitコマンドで実現せよ．


# coding: utf-8 素人の言語処理100本ノック模範解答
import math

fname = 'hightemp.txt'
n = int(input('N--> '))

with open(fname) as data_file:
    lines = data_file.readlines()

count = len(lines)
unit = math.ceil(count / n)  # 1ファイル当たりの行数

for i, offset in enumerate(range(0, count, unit), 1):
    with open('child_{:02d}.txt'.format(i), mode='w') as out_file:
        for line in lines[offset:offset + unit]:
            out_file.write(line)

# import nltk
# import numpy as np #numpyで2次元配列にする
# def split_n_file(n):
#   f = open('hightemp.txt')
#   document = f.read()
#   doc_token = nltk.word_tokenize(document)
#   doc_2d = np.array(doc_token).reshape((24,4)) #24行4列 ndarrayにする

#   path_w = '/Users/yamadahikaru/Projects/ML_Projects_Python/nlp100/chapter2/split_n.txt'
#   for r in row_n:
#     r = doc_2d[(int(n),:)] #1~n行目を抜き出したもの

#     for l in row_n:
#       with open(path_w, mode='w') as f:
#         f.write(' '.join(l))
#       with open(path_w) as f:
#         print(f.read())

# n = input("自然数(半角数字)を入力してください: ")
# split_n_file(n)
