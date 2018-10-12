# 42. 係り元と係り先の文節の表示
# 係り元の文節と係り先の文節のテキストをタブ区切り形式ですべて抽出せよ．ただし，句読点などの記号は出力しないようにせよ．

import nlp40
import nlp41

dst = nlp41.Chunk.self.dst
srcs = nlp41.Chunk.srcs
#係り先文節インデックス番号（dst），係り元文節インデックス番号のリスト（srcs）を使う
# def extract_relation(dst, srcs):



