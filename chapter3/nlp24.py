# 24. ファイル参照の抽出
# 記事から参照されているメディアファイルをすべて抜き出せ．
import nlp20
import re

data_uk = nlp20.read_uk('text').splitlines()
pattern1 = r'ファイル:'
pattern2 = r'File:'

for line in data_uk:
  matchmd1 = re.search(pattern1, line)
  matchmd2 = re.search(pattern2, line)
  if matchmd1 or matchmd2:
    print(line)

