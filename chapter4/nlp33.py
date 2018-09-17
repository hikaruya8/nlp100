# 33. サ変名詞
# サ変接続の名詞をすべて抽出せよ．

import nlp30

nlp30.parse_neko()

lines = nlp30.neko_lines()
noun_sahen = []
for line in lines:
  for morpheme in line:
    if (morpheme['pos'] == '名詞' and morpheme['pos1'] == 'サ変接続') and not morpheme['surface'] == '——':
      noun_sahen.append(morpheme['surface'])

print(noun_sahen)