import networkx as nx
import matplotlib.pyplot as plt


def task(inc, start=1):


    visited = []  # Посещена ли вершина?

    # Поиск в глубину - ПВГ (Depth First Search - DFS)
    def dfs(v):
        draw(inc, visited)
        if v in visited:  # Если вершина уже посещена, выходим
            return
        visited.append(v)  # Посетили вершину v
        for i in inc[v]:  # Все смежные с v вершины
            if not i in visited:
                dfs(i)

    dfs(start)  # start - начальная вершина обхода
    draw(inc, visited)



def draw(inc, visited):
    G = nx.DiGraph()
    vertexs = set()
    for key, value in inc.items():
        # print(f"{key} {value}")
        vertexs.add(key)
        for item in value:
            G.add_edge(key, item)
            vertexs.add(item)
    vertexs = list(vertexs)
    # print(vertexs)
    color_map = []
    for vertex in vertexs:
        if vertex in visited:
            color_map.append("red")
        else:
            color_map.append("blue")
    nx.draw_shell(G, node_color=color_map, with_labels=True)
    # plt.savefig("filename.png")
    from time import sleep
    sleep(1)
    plt.show()
    print(f"sequence: {visited}")


def test():
    G = nx.DiGraph()
    G.add_edge(1, 2)
    G.add_edge(1, 3)
    G.add_edge(1, 4)
    G.add_edge(1, 1)
    G.add_node(1)
    G.add_node(2)
    G.add_node(3)
    G.add_node(4)
    color_map = ["red", "red", "blue", "red"]

    nx.draw(G, node_color=color_map, with_labels=True)
    # plt.savefig("filename.png")
    plt.show()


if __name__ == "__main__":
    # Смежность вершин
    # inc = {
    #     1: [2, 8],
    #     2: [1, 3, 8],
    #     3: [2, 4, 8],
    #     4: [3, 7, 9],
    #     5: [6, 7],
    #     6: [5],
    #     7: [4, 5, 8],
    #     8: [1, 2, 3, 7],
    #     9: [4],
    # }
    inc = {
        1: [2],
        2: [3],
        3: [5,3],
        4: [4],
        5: [1],
        6: [6],
        7: [7],
    }
    task(inc, 1)