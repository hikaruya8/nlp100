# 16. ファイルをN分割する
# 自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．同様の処理をsplitコマンドで実現せよ．

import pandas as pd

def main():
    df = pd.read_csv('hightemp.txt', header=None)
    df.to_csv('split_n.csv', header=False, index=False, columns=range(0, 4))
    df.to_csv('iris_target_train.csv', header=False, index=False, columns=range(4, 5))

if __name__ == '__main__':
    main()
# def split_n_file(n):
#   f = open('hightemp.txt')
#   document = f.read()
#   doc_token = nltk.word_tokenize(document)
#   doc_2d = np.array(doc_token).reshape((24,4)) #24行4列 ndarrayにする

#   row_n = doc_2d[(-int(n)):,:] #1~n行目を抜き出したもの


#   path_w = '/Users/yamadahikaru/Projects/ML_Projects_Python/nlp100/chapter2/split_n.txt'

#   for l in row_n:
#     with open(path_w, mode='w') as f:
#       f.write(' '.join(l))
#     with open(path_w) as f:
#       print(f.read())

# n = input("自然数(半角数字)を入力してください: ")
# split_n_file(n)
