# 37. 頻度上位10語
# 出現頻度が高い10語とその出現頻度をグラフ（例えば棒グラフなど）で表示せよ．

import nlp36
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.family'] = 'AppleGothic'

line_common_words = nlp36.line_common_words()

ten_common_words = []
for i, line in enumerate(line_common_words):
  if i < 10:
    ten_common_words.append(line)
  else:
    break


# x, y = map(list, zip(*ten_common_words))
x = np.array(ten_common_words)[0:,0]
y = np.array(ten_common_words)[0:,1]
print(x)
print(y)

plt.bar(range(len(x)), y, tick_label=x, align="center")

plt.show()

