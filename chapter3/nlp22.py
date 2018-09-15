# 22. カテゴリ名の抽出
# 記事のカテゴリ名を（行単位ではなく名前で）抽出せよ．

import nlp20

data_uk = nlp20.read_uk('text').splitlines()
for d in data_uk:
  if 'Category' in d:
    l = d.find('|')
    if not l == -1:
      print(d[11:l])
    else:
      print(d[11:-2])