import from44
from from44 import Chunk
import pydot

fname = 'neko.txt.tmp'
fname_parsed = 'neko.txt.cabocha.tmp'

def graph_from_edges_ex(edge_list, directed=False):
    '''pydot_ng.graph_from_edges()のノード識別子への対応版

    graph_from_edges()のedge_listで指定するタプルは
    識別子とグラフ表示時のラベルが同一のため、
    ラベルが同じだが実体が異なるノードを表現することができない。
    例えば文の係り受けをグラフにする際、文の中に同じ単語が
    複数出てくると、それらのノードが同一視されて接続されてしまう。

    この関数ではedge_listとして次の書式のタプルを受け取り、
    ラベルが同一でも識別子が異なるノードは別ものとして扱う。

    edge_list = [((識別子1,ラベル1),(識別子2,ラベル2)), ...]

    識別子はノードを識別するためのもので表示されない。
    ラベルは表示用で、同じでも識別子が異なれば別のノードになる。

    なお、オリジナルの関数にあるnode_prefixは未実装。

    戻り値：
    pydot.Dotオブジェクト
    '''

    if directed:
        graph = pydot.Dot(graph_type='digraph')

    else:
        graph = pydot.Dot(graph_type='graph')

    for edge in edge_list:

        id1 = str(edge[0][0])
        label1 = str(edge[0][1])
        id2 = str(edge[1][0])
        label2 = str(edge[1][1])

        # ノード追加
        graph.add_node(pydot.Node(id1, label=label1))
        graph.add_node(pydot.Node(id2, label=label2))

        # エッジ追加
        graph.add_edge(pydot.Edge(id1, id2))

    return graph


# 対象文字列を入力してもらい、そのままfnameに保存
with open(fname, mode='w') as out_file:
    out_file.write(input('文字列を入力してください--> '))

# 係り受け解析
from44.parse_neko()

# 1文ずつリスト作成
for chunks in from44.neko_lines():

    # 係り先があるものを列挙
    edges = []
    for i, chunk in enumerate(chunks):
        if chunk.dst != -1:

            # 記号を除いた表層形をチェック、空なら除外
            src = chunk.normalized_surface()
            dst = chunks[chunk.dst].normalized_surface()
            if src != '' and dst != '':
                edges.append(((i, src), (chunk.dst, dst)))

    # 描画
    if len(edges) > 0:
        graph = graph_from_edges_ex(edges, directed=True)
        graph.write_png('result.png')