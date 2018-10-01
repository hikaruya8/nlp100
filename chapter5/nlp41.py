# 41. 係り受け解析結果の読み込み（文節・係り受け）
# 40に加えて，文節を表すクラスChunkを実装せよ．このクラスは形態素（Morphオブジェクト）のリスト（morphs），係り先文節インデックス番号（dst），係り元文節インデックス番号のリスト（srcs）をメンバ変数に持つこととする．さらに，入力テキストのCaboChaの解析結果を読み込み，１文をChunkオブジェクトのリストとして表現し，8文目の文節の文字列と係り先を表示せよ．第5章の残りの問題では，ここで作ったプログラムを活用せよ．

import nlp40

class Chunk():
  # 形態素（Morphオブジェクト）のリスト（morphs），係り先文節インデックス番号（dst），係り元文節インデックス番号のリスト（srcs）をメンバ変数に持つ
  def __init__(self, morphs, dst, srcs):
    #メンバ変数
    self.morphs = morphs
    self.dst = dst
    self.srcs = srcs

if __name__ == '__main__':
  for i, morphs in enumerate(nlp40.relate_lines(), 1):
    # 3文目を表示
    if i == 8:
      for morph in morphs:
        print(morph)
      break