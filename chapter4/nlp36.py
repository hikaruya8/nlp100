# 36. 単語の出現頻度
# 文章中に出現する単語とその出現頻度を求め，出現頻度の高い順に並べよ

import nlp30
import collections

def line_common_words():
  lines = nlp30.neko_lines()
  words = []
  for line in lines:
    for morpheme in line:
      words.append(morpheme['surface'])

  word_count = collections.Counter(words)

  common_words = word_count.most_common()

  yield common_words

