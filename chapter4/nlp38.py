# 38. ヒストグラム
# 単語の出現頻度のヒストグラム（横軸に出現頻度，縦軸に出現頻度をとる単語の種類数を棒グラフで表したもの）を描け．

import nlp36
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.family'] = 'AppleGothic'

line_common_words = nlp36.line_common_words()

hundred_common_words = [] #とりあえず100で考えてみる
for i, line in enumerate(line_common_words):
  if i < 100:
    hundred_common_words.append(line)
  else:
    break

x = np.array(hundred_common_words)[0:,0]
y = np.array(hundred_common_words)[0:,1]
print(x)
print(y)

plt.hist(x, y, tick_label=x)
plt.show()