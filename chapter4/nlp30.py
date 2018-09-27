# 30. 形態素解析結果の読み込み
# 形態素解析結果（neko.txt.mecab）を読み込むプログラムを実装せよ．ただし，各形態素は表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）をキーとするマッピング型に格納し，1文を形態素（マッピング型）のリストとして表現せよ．第4章の残りの問題では，ここで作ったプログラムを活用せよ．

import MeCab
import sys

fname = 'neko.txt'
fname_parsed = 'neko.txt.mecab'

def parse_neko():
  #neko.txtを形態素解析してneko.txt.mecabに取り込む
  with open(fname) as data_file, open(fname_parsed, mode='w') as out_file:
    mecab = MeCab.Tagger()
    out_file.write(mecab.parse(data_file.read()))

def neko_lines():
  '''「吾輩は猫である」の形態素解析結果のジェネレータ
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
if __name__ == "parse_neko":
  parse_neko()

# 1文ずつ辞書のリストを作成
if __name__ == "__neko_lines__":
  lines = neko_lines()
  for line in lines:
      print(line)

