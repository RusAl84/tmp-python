import networkx as nx
import matplotlib.pyplot as plt


class ADTgrapth:
    def __init__(self):
        # https://www.geeksforgeeks.org/python-visualize-graphs-generated-in-networkx-using-matplotlib/
        self.g = nx.Graph()
        self.edges = []
        self.edge_labels = {}
        self.node_labels = {}

    # ADD_V(<имя>, <метка, mark, weight>) - добавить УЗЕЛ
    def addV(self, name, marker=""):
        self.g.add_node(name)
        self.node_labels[name] = marker

    # ADD_Е(v, w, c) - добавить ДУГУ (здесь c — вес, цена дуги (v,w))
    def addE(self, startV, endV, label=""):
        edge = [startV, endV]
        self.edges.append(edge)
        self.edge_labels[label] = (startV, endV)

    # FIRST(v) - возвращает индекс первой вершины, смежной с вершиной v. Если вершина v не имеет смежных вершин, то возвращается "нулевая" вершина ?.
    def first(self, v):
        result = ""
        for item in self.edges:
            if item[0] == v:
                result = item[1]
                break;
        return result

    # NEXT(v, i)- возвращает индекс вершины, смежной с вершиной v, следующий за индексом i. Если i — это индекс последней вершины, смежной с вершиной v, то возвращается ?.
    # VERTEX(v, i) - возвращает вершину с индексом i из множества вершин, смежных с v.
    # DEL_V(<имя>) - удалить УЗЕЛ
    # DEL_Е(v, w) – удалить ДУГУ
    # EDIT_V(<имя>, <новое значение метки или маркировки>) - изменить метку (маркировку) УЗЛА
    # EDIT_Е(v, w, <новый вес дуги>) - изменить вес ДУГИ

    def draw(self):
        self.g.add_edges_from(self.edges)
        pos = nx.circular_layout(self.g)
        self.edge_labels = {v: k for k, v in self.edge_labels.items()}
        nx.draw_networkx_edge_labels(
            self.g, pos,
            edge_labels=self.edge_labels,
            font_color='red'
        )
        nx.draw_networkx_labels(self.g, pos, self.node_labels, font_size=16, font_color='r')
        nx.draw_shell(self.g, with_labels=True, )
        # draw_circular(G, keywords) : This gives circular layout of the graph G.
        # draw_planar(G, keywords) :] This gives a planar layout of a planar networkx graph G.
        # draw_random(G, keywords) : This gives a random layout of the graph G.
        # draw_spectral(G, keywords) : This gives a spectral 2D layout of the graph G.
        # draw_spring(G, keywords) : This gives a spring layout of the graph G.
        # draw_shell(G, keywords) : This gives a shell layout of the graph G.
        # plt.savefig("filename.png")
        plt.show()


def example_graph_a_cat(g):
    g.addV('A')
    g.addV('B')
    g.addV('C')
    g.addV('D')
    g.addV('E')
    g.addV('F')
    g.addV('G')
    g.addV('H')
    g.addV('K')
    g.addV('L')
    g.addE('A', 'C')
    g.addE('B', 'C')
    g.addE('D', 'C')
    g.addE('C', 'E')
    g.addE('F', 'E')
    g.addE('G', 'E')
    g.addE('H', 'E')
    g.addE('H', 'K')
    g.addE('H', 'L')
    g.addE('H', 'M')


if __name__ == "__main__":
    g = ADTgrapth()
    example_graph_a_cat(g)

    print(g.first("A")) #test first function
    g.draw()
