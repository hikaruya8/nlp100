# 第5章: 係り受け解析
# 夏目漱石の小説『吾輩は猫である』の文章（neko.txt）をCaboChaを使って係り受け解析し，その結果をneko.txt.cabochaというファイルに保存せよ．このファイルを用いて，以下の問に対応するプログラムを実装せよ．

# 40. 係り受け解析結果の読み込み（形態素）
# 形態素を表すクラスMorphを実装せよ．このクラスは表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）をメンバ変数に持つこととする．さらに，CaboChaの解析結果（neko.txt.cabocha）を読み込み，各文をMorphオブジェクトのリストとして表現し，3文目の形態素列を表示せよ．

import CaboCha
import sys

fname = '/Users/yamadahikaru/Projects/ML_Projects_Python/nlp100/chapter4/neko.txt'
fname_parsed = 'neko.txt.cabocha'

def relate_neko():
  #neko.txtを係り受け解析してneko.txt.cabochaに取り込む
  with open(fname) as data_file, open(fname_parsed, mode='w') as out_file:
    cabocha = CaboCha.Parser()
    for line in data_file:
      out_file.write(cabocha.parse(line).toString(CaboCha.FORMAT_LATTICE))

class Morph:
    '''
    形態素クラス
    表層形（surface）、基本形（base）、品詞（pos）、品詞細分類1（pos1）を
    メンバー変数に持つ
    '''
    def __init__(self, surface, base, pos, pos1):
        '''初期化'''
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

    def __str__(self):
        '''オブジェクトの文字列表現'''
        return 'surface[{}]\tbase[{}]\tpos[{}]\tpos1[{}]'\
            .format(self.surface, self.base, self.pos, self.pos1)

def relate_lines():
    '''「吾輩は猫である」の係り受け解析結果のジェネレータ
    「吾輩は猫である」の係り受け解析結果を順次読み込んで、
    1文ずつMorphクラスのリストを返す

    戻り値：
    1文のMorphクラスのリスト
    '''
    with open(fname_parsed) as file_parsed:

        morphs = []
        for line in file_parsed:

            # 1文の終了判定
            if line == 'EOS\n':
                yield morphs
                morphs = []

            else:
                # 先頭が*の行は係り受け解析結果なのでスキップ
                if line[0] == '*':
                    continue

                # 表層形はtab区切り、それ以外は','区切りでバラす
                cols = line.split('\t')
                res_cols = cols[1].split(',')

                # Morph作成、リストに追加
                morphs.append(Morph(
                    cols[0],        # surface
                    res_cols[6],    # base
                    res_cols[0],    # pos
                    res_cols[1]     # pos1
                ))

        raise StopIteration


if __name__ == '__main__':
  # 形態素解析
  relate_neko()

  # 1文ずつリスト作成
  for i, morphs in enumerate(relate_lines(), 1):

      # 3文目を表示
      if i == 3:
          for morph in morphs:
              print(morph)
          break