# 34. 「AのB」
# 2つの名詞が「の」で連結されている名詞句を抽出せよ．

import nlp30

lines = nlp30.neko_lines()
nouns_a_no_b = []
for line in lines:
  if len(line) > 2:
    for i in range(1, len(line) - 1):
      if line[i]['surface'] == 'の' \
        and line[i-1]['pos'] == '名詞' \
        and line[i+1]['pos'] == '名詞':
        nouns_a_no_b.append(line[i-1]['surface']+'の'+line[i+1]['surface'])
a_no_b = set(nouns_a_no_b)


sorted_a_no_b = sorted(a_no_b, key=nouns_a_no_b.index)
print(sorted_a_no_b)