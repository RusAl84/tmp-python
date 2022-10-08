def task(inc, v=1):
    visited = []  # Посещена ли вершина?

    # Поиск в глубину - ПВГ (Depth First Search - DFS)
    def dfs(v):
        if v in visited:  # Если вершина уже посещена, выходим
            return
        visited.append(v)  # Посетили вершину v
        for i in inc[v]:  # Все смежные с v вершины
            if not i in visited:
                dfs(i)

    dfs(v)  # start - начальная вершина обхода
    return visited


if __name__ == "__main__":
    # Определить k-связанность заданного неориентированного графа и
    # вывести полученное число k на экран.
    # (Граф называется k-связным, если между любой парой вершин
    # v и w существует не менее k разных путей, таких, что,
    # за исключением вершин v и w, ни одна из вершин, входящих
    # в один путь, не входит ни в какой другой из этих путей).
    adjacency = [[1, 1, 0, 0, 0, 0, 0],
                 [0, 0, 1, 0, 0, 0, 0],
                 [0, 0, 1, 0, 1, 0, 0],
                 [0, 0, 0, 1, 0, 0, 0],
                 [0, 0, 0, 0, 1, 0, 0],
                 [0, 0, 0, 0, 0, 1, 0],
                 [0, 0, 0, 0, 0, 0, 1]]
    inc1 = {}
    num_x = 1
    for x in adjacency:
        num_y = 1
        l_y=[]
        for y in x:
            if y == 1:
                l_y.append(num_y)
            num_y += 1
        inc1[num_x] = l_y
        num_x += 1
    print(inc1)

    inc = {
        1: [1, 2],
        2: [3],
        3: [3, 5],
        4: [4],
        5: [1],
        6: [6],
        7: [7],
    }
    print(inc)
    af = []
    for v in range(1, len(inc) + 1):
        l = task(inc, v)
        l = sorted(l)
        af.append(l)
    print(af)
    vivo = set()
    for item in af:
        vivo.add(str(item))
    print(vivo)
    print(f"Количество связных компонент: {len(vivo)}")
