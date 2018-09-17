# 32. 動詞の原形
# 動詞の原形をすべて抽出せよ

import nlp30

lines = nlp30.neko_lines()
verbs = []
for line in lines:
  for morpheme in line:
    if morpheme['pos'] == '動詞':
      verbs.append(morpheme['base'])

print(verbs)