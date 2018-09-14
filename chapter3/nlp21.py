# 21. カテゴリ名を含む行を抽出
# 記事中でカテゴリ名を宣言している行を抽出せよ．

import nlp20

data_uk = nlp20.read_uk('text').splitlines()
for d in data_uk:
  if 'Category' in d:
    print(d)

