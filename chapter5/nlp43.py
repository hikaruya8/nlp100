# 43. 名詞を含む文節が動詞を含む文節に係るものを抽出
# 名詞を含む文節が，動詞を含む文節に係るとき，これらをタブ区切り形式で抽出せよ．ただし，句読点などの記号は出力しないようにせよ．

import nlp40
import nlp41
from nlp41 import Chunk
import nlp42

nlp40.relate_neko()

for chunks in nlp41.neko_lines():
  for chunk in chunks:
    if chunk.dst != -1:
      src = chunk.normalized_surface()
      dst = chunks[chunk.dst].normalized_surface()
      if src != '' and dst != '' and nlp40.morphs[pos] == '名詞':
        print('{}\t{}'.format(src, dst))