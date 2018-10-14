# 41. 係り受け解析結果の読み込み（文節・係り受け）
# 40に加えて，文節を表すクラスChunkを実装せよ．このクラスは形態素（Morphオブジェクト）のリスト（morphs），
# 係り先文節インデックス番号（dst），係り元文節インデックス番号のリスト（srcs）をメンバ変数に持つこととする．
# さらに，入力テキストのCaboChaの解析結果を読み込み，１文をChunkオブジェクトのリストとして表現し，
# 8文目の文節の文字列と係り先を表示せよ．第5章の残りの問題では，ここで作ったプログラムを活用せよ．

import nlp40
import re

fname = '/Users/yamadahikaru/Projects/ML_Projects_Python/nlp100/chapter4/neko.txt'
fname_parsed = 'neko.txt.cabocha'

class Chunk:
  # 形態素（Morphオブジェクト）のリスト（morphs），係り先文節インデックス番号（dst），係り元文節インデックス番号のリスト（srcs）をメンバ変数に持つ
  def __init__(self):
    #初期化
    self.morphs = []
    self.srcs = []
    self.dst = -1

  def __str__(self):
    '''オブジェクトの文字列表現'''
    surface = ''
    for morph in self.morphs:
        surface += morph.surface
    return '{}\tsrcs{}\tdst[{}]'.format(surface, self.srcs, self.dst)

  def normalized_surface(self):
      #句読点などの記号を出力しないようにする
      result = ''
      for morph in self.morphs:
          if morph in self.morphs:
              if morph.pos != '記号':
                  result += morph.surface
              return result
  def chk_pos(self, pos):
    '''指定した品詞（pos）を含むかチェックする

    戻り値：
    品詞（pos）を含む場合はTrue
    '''
    for morph in self.morphs:
      if morph.pos == pos:
        return True
    return False


def neko_lines():
  # 「吾輩は猫である」の係り受け解析結果のジェネレータ
  # 「吾輩は猫である」の係り受け解析結果を順次読み込んで、
  # 1文ずつChunkクラスのリストを返す

  # 戻り値：
  # 1文のChunkクラスのリスト

  with open(fname_parsed) as file_parsed:
    chunks = dict()
    idx = -1

    for line in file_parsed:
      if line == 'EOS\n':

        if len(chunks) > 0:
          sorted_tuple = sorted(chunks.items(), key=lambda x:x[0])
          yield list(zip(*sorted_tuple))[1]
          chunks.clear()

        else:
          yield []

      # 先頭が*の行は係り受け解析結果なので、Chunkを作成
      elif line[0] == '*':

        # Chunkのインデックス番号と係り先のインデックス番号取得
        cols = line.split(' ')
        idx = int(cols[1])
        dst = int(re.search(r'(.*?)D', cols[2]).group(1))

        # Chunkを生成（なければ）し、係り先のインデックス番号セット
        if idx not in chunks:
          chunks[idx] = Chunk()
        chunks[idx].dst = dst

        # 係り先のChunkを生成（なければ）し、係り元インデックス番号追加
        if dst != -1:
          if dst not in chunks:
            chunks[dst] = Chunk()
          chunks[dst].srcs.append(idx)

      # それ以外の行は形態素解析結果なので、Morphを作りChunkに追加
      else:

          # 表層形はtab区切り、それ以外は','区切りでバラす
        cols = line.split('\t')
        res_cols = cols[1].split(',')

        # Morph作成、リストに追加
        chunks[idx].morphs.append(
            nlp40.Morph(
                cols[0],        # surface
                res_cols[6],    # base
                res_cols[0],    # pos
                res_cols[1]     # pos1
            )
          )

  raise StopIteration


if __name__ == '__main__':
  nlp40.relate_neko()

    # 1文ずつリスト作成
  for i, chunks in enumerate(neko_lines(), 1):
    # 8文目を表示
    if i == 8:
      for j, chunk in enumerate(chunks):
          print('[{}]{}'.format(j, chunk))
      break
