# 11. タブをスペースに置換
# タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．
tab = '  '
space = ' '

def tab_space(document):
  for d in document:
    if tab in d:
      


document = input('タブを含んだ文字列を入力してください')
tab_space(document)