# 35. 名詞の連接
# 名詞の連接（連続して出現する名詞）を最長一致で抽出せよ

import nlp30

lines = nlp30.neko_lines()

list_articulated_nouns = []
list_nouns = []

for line in lines:
  if len(line) > 1:
    for i in range(1, len(line)-1):
      if line[i]['pos'] == '名詞' \
      and line[i+1]['pos'] == '名詞':
        list_articulated_nouns.append(line[i]['surface'])
      elif line[i]['pos'] == None:
        break

print(list_articulated_nouns)
