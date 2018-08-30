# 08. 暗号文
# 与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．

# 英小文字ならば(219 - 文字コード)の文字に置換
# その他の文字はそのまま出力
# この関数を用い，英語のメッセージを暗号化・復号化せよ

def cipher(target):
  result = ''
  
  for t in target:
    if t.islower():
      result += chr(219 - ord(t))

    else:
      result += t
  return result

# 対象文字列の入力
target = input('文字列を入力してください--> ')

# 暗号化
result = cipher(target)
print('暗号化:' + result)

# 復号化
result2 = cipher(result)
print('復号化:' + result2)

# 復号化で元に戻っているかチェック
if result2 != target:
    print('元に戻っていない！？')