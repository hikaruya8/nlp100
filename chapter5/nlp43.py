# 43. 名詞を含む文節が動詞を含む文節に係るものを抽出
# 名詞を含む文節が，動詞を含む文節に係るとき，これらをタブ区切り形式で抽出せよ．ただし，句読点などの記号は出力しないようにせよ．
import nlp40
import nlp41
from nlp41 import Chunk

nlp40.relate_neko()
  # 1文ずつリスト作成
for chunks in nlp41.neko_lines():
  for chunk in chunks:
    if chunk.dst != -1:
      #かかり元に名詞があるか、係り先に動詞があるかチェック
        if chunk.chk_pos('名詞') and chunks[chunk.dst].chk_pos('名詞'):
          src = chunk.normalized_surface()
          dst = chunks[chunk.dst].normalized_surface()
          if src != '' and dst != '':
            print('{}\t{}'.format(src, dst))