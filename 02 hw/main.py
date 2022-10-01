import networkx as nx
import matplotlib.pyplot as plt


class ADTgrapth:
    def __init__(self):
        # https://www.geeksforgeeks.org/python-visualize-graphs-generated-in-networkx-using-matplotlib/
        self.g = nx.Graph()

    # ADD_V(<имя>, <метка, mark>) - добавить УЗЕЛ
    def addV(self, name, mark):
        self.g.add_node(name, )

    # FIRST(v) - возвращает индекс первой вершины, смежной с вершиной v. Если вершина v не имеет смежных вершин, то возвращается "нулевая" вершина ?.
    # NEXT(v, i)- возвращает индекс вершины, смежной с вершиной v, следующий за индексом i. Если i — это индекс последней вершины, смежной с вершиной v, то возвращается ?.
    # VERTEX(v, i) - возвращает вершину с индексом i из множества вершин, смежных с v.

    # ADD_Е(v, w, c) - добавить ДУГУ (здесь c — вес, цена дуги (v,w))
    # DEL_V(<имя>) - удалить УЗЕЛ
    # DEL_Е(v, w) – удалить ДУГУ
    # EDIT_V(<имя>, <новое значение метки или маркировки>) - изменить метку (маркировку) УЗЛА
    # EDIT_Е(v, w, <новый вес дуги>) - изменить вес ДУГИ

    def add(self, x, y):
        self.g.add_edge(x, y)

    def draw(self):
        nx.draw_circular(self.g, with_labels=True)
        # draw_circular(G, keywords) : This gives circular layout of the graph G.
        # draw_planar(G, keywords) :] This gives a planar layout of a planar networkx graph G.
        # draw_random(G, keywords) : This gives a random layout of the graph G.
        # draw_spectral(G, keywords) : This gives a spectral 2D layout of the graph G.
        # draw_spring(G, keywords) : This gives a spring layout of the graph G.
        # draw_shell(G, keywords) : This gives a shell layout of the graph G.
        # plt.savefig("filename.png")
        plt.show()


if __name__ == "__main__":
    g = ADTgrapth()
    g.add('a', 'b')
    g.add('a', 'c')
    g.add('a', 'd')
    g.draw()
