# 08. 暗号文
# 与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．

# 英小文字ならば(219 - 文字コード)の文字に置換
# その他の文字はそのまま出力
# この関数を用い，英語のメッセージを暗号化・復号化せよ
result = ''

def chiper(target):
  for t in target:
    if t.islower():
      result = chr(219 - ord(t))

    else:
      result = t
  return result

target = input('文字列を入力してください')
chiper(target)