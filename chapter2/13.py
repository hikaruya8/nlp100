# 13. col1.txtとcol2.txtをマージ
# 12で作ったcol1.txtとcol2.txtを結合し，元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．確認にはpasteコマンドを用いよ．

# import glob
# import subprocess

# for f in glob.glob("col*.txt"):
#   subprocess.call("cat "+f+" >> OutFile.txt", shell=True)
# 上は羅列だけになってる

with open("col1.txt") as col1_file, \
     open("col2.txt") as col2_file, \
     open("merge.txt", mode="w") as out_file:

     for col1_line, col2_line in zip(col1_file, col2_file):
        out_file.write(col1_line.rstrip() + '\t' + col2_line.rstrip() + '\n')