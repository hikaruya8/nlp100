# 42. 係り元と係り先の文節の表示
# 係り元の文節と係り先の文節のテキストをタブ区切り形式ですべて抽出せよ．ただし，句読点などの記号は出力しないようにせよ．

import nlp40
import nlp41
from nlp41 import Chunk

#nlp41のChunkクラスに関数normalized_surface()を追加

if __name__ == '__main__':
  nlp40.relate_neko()
  # 1文ずつリスト作成
  for chunks in nlp41.neko_lines():
    for chunk in chunks:
      if chunk.dst != -1:
        src = chunk.normalized_surface()
        dst = chunks[chunk.dst].normalized_surface()
        if src != '' and dst != '':
            print('{}\t{}'.format(src, dst))




#係り先文節インデックス番号（dst），係り元文節インデックス番号のリスト（srcs）を使う
# def extract_relation(dst, srcs):
