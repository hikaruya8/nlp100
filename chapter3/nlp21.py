# 21. カテゴリ名を含む行を抽出
# 記事中でカテゴリ名を宣言している行を抽出せよ．

import pandas as pd
import numpy as np
import re
import nlp20

# data = pd.read_json('/Users/yamadahikaru/Projects/ML_Projects_Python/nlp100/chapter3/jawiki-country.json.gz', lines=True)
# rown = data.text.loc[1]#pandas.read_jsonのオプションを読む
# # Category_row = rown.loc[]

data_uk = nlp20.read_uk('text')
itr_data_uk = re.finditer('Category', data_uk)
for i in itr_data_uk:
  print(i)




