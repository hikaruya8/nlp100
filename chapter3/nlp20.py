# 20. JSONデータの読み込み
# Wikipedia記事のJSONファイルを読み込み，「イギリス」に関する記事本文を表示せよ．問題21-29では，ここで抽出した記事本文に対して実行せよ．

import gzip
import json

def read_json(read_key):
  with gzip.open('jawiki-country.json.gz', 'rt') as data:
    for line in data:
      data_json = json.loads(line)
      if data_json['title'] == 'イギリス':
        return data_json[read_key]
        break

read_json('text')