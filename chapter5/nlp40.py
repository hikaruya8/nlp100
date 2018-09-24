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

def relate_lines():
  '''「吾輩は猫である」の係り受け解析結果のジェネレータ
  「吾輩は猫である」の形態素解析結果を順次読み込んで、各形態素を
  ・表層形（surface）
  ・基本形（base）
  ・品詞（pos）
  ・品詞細分類1（pos1）
  の4つをキーとする辞書に格納し、1文ずつ、この辞書のリストとして返す

  戻り値：
  1文の各形態素を辞書化したリスト
  '''
  with open(fname_parsed) as file_parsed:
    morphemes = []
    for line in file_parsed:
      #表層形はtabで区切る、それ以外は','で区切る
      cols = line.split('\t')
      if len(cols) < 2:
        raise StopIteration #区切りがない場合終了
      res_cols = cols[1].split(',')

      #辞書を作成し、辞書に追加 詳細は表層形\t品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用型,活用形,原形,読み,発音
      #http://taku910.github.io/mecab/#format

      morpheme = {
        'surface': cols[0],
        'base': res_cols[6],
        'pos': res_cols[0],
        'pos1': res_cols[1]
      }
      morphemes.append(morpheme)

      # 品詞細分類1が'句点'なら文の終わりと判定
      if res_cols[1] == '句点':
        yield morphemes #大きいデータはreturnで一度に引き渡すのではなく、yeildで少量ずつ読み込む
        morphemes = []

# 形態素解析
relate_neko()

# # 1文ずつ辞書のリストを作成
# lines = neko_lines()
# for line in lines:
#     print(line)