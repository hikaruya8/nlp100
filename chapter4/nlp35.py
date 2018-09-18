# 35. 名詞の連接
# 名詞の連接（連続して出現する名詞）を最長一致で抽出せよ

import nlp30

lines = nlp30.neko_lines()

list_series_noun = []

for line in lines:
  nouns = []
  for morpheme in line:
    if morpheme['pos'] == '名詞':
      nouns.append(morpheme['surface'])
    else:
      if len(nouns) > 1:
        list_series_noun.append("".join(nouns))
        nouns = []
  if len(nouns) > 1:
    list_series_noun.append("".join(nouns))

series_noun = set(list_series_noun)

print(sorted(series_noun, key=list_series_noun.index))