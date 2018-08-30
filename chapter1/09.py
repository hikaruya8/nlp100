# 09. Typoglycemia
# スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．ただし，長さが４以下の単語は並び替えないこととする．適当な英語の文（例えば"I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."）を与え，その実行結果を確認せよ

import nltk
import random

def typoglycemia(document):
  result = ''
  doc = document
  doc_tokens = nltk.word_tokenize(doc)
  for t in doc_tokens:
    if len(t) <= 4: #単語の長さが４文字以下の場合そのまま出力
      result += ' ' + t
    else:           #単語の長さが５以上ならば先頭と末尾の文字は残し，それ以外の文字の順序をランダムに並び替える
      sr = ''.join(random.sample(t[1:-1], len(t[1:-1])))
      result += ' ' + (t[0] + sr + t[-1])
  return result

document = input("文字列を入力してください->")
print(typoglycemia(document))


