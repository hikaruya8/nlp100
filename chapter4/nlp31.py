# 31. 動詞
# 動詞の表層形をすべて抽出せよ．

import nlp30

lines = nlp30.neko_lines()
verbs = []
for line in lines:
  for morpheme in line:
    if morpheme['pos'] == '動詞':
      verbs.append(morpheme['surface'])

print(verbs)
