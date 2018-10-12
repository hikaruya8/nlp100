# 42. 係り元と係り先の文節の表示
# 係り元の文節と係り先の文節のテキストをタブ区切り形式ですべて抽出せよ．ただし，句読点などの記号は出力しないようにせよ．

import nlp40
import nlp41
from nlp41 import Chunk

nlp40.relate_neko()
# 1文ずつリスト作成
for i, chunks in enumerate(nlp41.neko_lines(), 1):
# 8文目を表示
    if i == 8:
        for j, chunk in enumerate(chunks):
            print('[{}]{}'.format(j, chunk))
        break


#係り先文節インデックス番号（dst），係り元文節インデックス番号のリスト（srcs）を使う
# def extract_relation(dst, srcs):
