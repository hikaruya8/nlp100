# 21. カテゴリ名を含む行を抽出
# 記事中でカテゴリ名を宣言している行を抽出せよ．

import nlp20 #20.pyファイルを使う
import pandas as pd
import numpy as np
import json

data = pd.read_json('/Users/yamadahikaru/Projects/ML_Projects_Python/nlp100/chapter3/jawiki-country.json.gz', lines=True)
rown = data.text.loc[1]#pandas.read_jsonのオプションを読む
Category_row = rown.loc[Category:オーストリア|*]

print(Category_row)



