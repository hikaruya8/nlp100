# 37. 頻度上位10語
# 出現頻度が高い10語とその出現頻度をグラフ（例えば棒グラフなど）で表示せよ．

import nlp36
import matplotlib.pyplot as plt
import numpy as np

line_common_words = nlp36.line_common_words()

for i, line in enumerate(line_common_words):
  if i < 10:
    print(i, line)
  else:
    break

