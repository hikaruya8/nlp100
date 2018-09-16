# 24. ファイル参照の抽出
# 記事から参照されているメディアファイルをすべて抜き出せ．
import nlp20
import re

data_uk = nlp20.read_uk('text')

pattern = re.compile(r'''
  (?:File|ファイル)
  :
  (.+?)
  \|
  ''', re.VERBOSE)

matchmd = pattern.findall(data_uk)
for line in matchmd:
  print(line)

