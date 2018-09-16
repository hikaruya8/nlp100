# 23. セクション構造
# 記事中に含まれるセクション名とそのレベル（例えば"== セクション名 =="なら1）を表示せよ．
# セクション名とは問題26で参考情報として紹介されているマークアップ早見表の「見出し」を指しているもよう
import nlp20
import re

data_uk = nlp20.read_uk('text')
pattern = re.compile(r'''
    ^       # 行頭
    (={2,}) # キャプチャ対象、2個以上の'='
    \s*     # 余分な0個以上の空白（'哲学'や'婚姻'の前後に余分な空白があるので除去）
    (.+?)   # キャプチャ対象、任意の文字が1文字以上、非貪欲（以降の条件の巻き込み防止）
    \s*     # 余分な0個以上の空白
    \1      # 後方参照、1番目のキャプチャ対象と同じ内容
    .*      # 任意の文字が0文字以上
    $       # 行末
    ''', re.MULTILINE + re.VERBOSE)


result = pattern.findall(data_uk)

for line in data_uk:
  level = len(line[0]) # '='の数-1
  print('{indent},{sect},{level}'.format(indent=('\t' * (level - 1)), sect=line[1], level=level))
