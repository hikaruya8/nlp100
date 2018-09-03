# 11. タブをスペースに置換
# タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．
document = open('hightemp.txt')

def tab_space(document):
  d_list = ''
  for doc in document:
    d = doc.expandtabs(1)
    d_list += d
  return d_list

print(tab_space(document))