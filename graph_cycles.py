N = int(input())  # число вершин в графе
G = []  # граф, матрица смежности

for i in range(N):
    row = list(map(int, input().split()))
    G.append(row)

# счетчики вхождений циклов
cycle3 = 0
cycle4 = 0
cycle5 = 0

orbits = [[0 for i in range(3)] for j in range(N)]  # G[i][0] кол-во вхождений в орбиту 3 (3-цикл)
                                                    # G[i][1] кол-во вхождений в орбиту 8 (4-цикл)
                                                    # G[i][2] кол-во вхождений в орбиту 34 (5-цикл)
# списки вершин и ребер каждого цикла
cycle3_list = []
cycle4_list = []
cycle5_list = []


# циклы длины 3

for i in range(0, N):
    for j in range(i + 1, N):
        if not G[i][j]:
            continue
        for k in range(j + 1, N):
            if G[j][k] and G[i][k]:  # найден цикл длины 3
                cycle3 += 1
                orbits[i][0] += 1
                orbits[j][0] += 1
                orbits[k][0] += 1

                vertices = [i, j, k]
                edges = [[i, j], [j, k], [i, k]]
                cycle = [vertices, edges]
                cycle3_list.append(cycle)


# циклы длины 4

for i in range(0, N):
    for j in range(0, N):
        if j == i or not G[i][j]:
            continue
        for k in range(0, N):
            if k == i or k == j or not G[j][k]:
                continue
            for p in range(0, N):
                if p == i or p == j or p == k:
                    continue
                if G[k][p] and G[i][p]:  # найден цикл длины 4
                    if not G[i][k] and not G[j][p]:  # проверим, что нет других ребер
                        cycle4 += 1
                        orbits[i][1] += 1
                        orbits[j][1] += 1
                        orbits[k][1] += 1
                        orbits[p][1] += 1

                        vertices = [i, j, k, p]
                        edges = [[i, j], [j, k], [k, p], [i, p]]
                        cycle = [vertices, edges]
                        cycle4_list.append(cycle)

# каждый цикл длины 4 обходим из каждой вершины и в разных направлениях, поэтому результат делим на 8
cycle4 = int(cycle4 / 8)
for i in range(N):
    orbits[i][1] = int(orbits[i][1] / 8)


# циклы длины 5

for i in range(0, N):
    for j in range(0, N):
        if j == i or not G[i][j]:
            continue
        for k in range(0, N):
            if k == i or k == j or not G[j][k]:
                continue
            for p in range(0, N):
                if p == i or p == j or p == k or not G[k][p]:
                    continue
                for d in range(0, N):
                    if d == i or d == j or d == k or d == p:
                        continue
                    if G[p][d] and G[i][d]:  # найден цикл длины 5
                        if not G[i][k] and not G[i][p] and not G[j][d] and not G[j][p] and not G[d][k]:  # проверим, что нет других ребер
                            cycle5 += 1
                            orbits[i][2] += 1
                            orbits[j][2] += 1
                            orbits[k][2] += 1
                            orbits[p][2] += 1
                            orbits[d][2] += 1

                            vertices = [i, j, k, p, d]
                            edges = [[i, j], [j, k], [k, p], [p, d], [i, d]]
                            cycle = [vertices, edges]
                            cycle5_list.append(cycle)

# каждый цикл длины 5 обходим из каждой вершины и в разных направлениях, поэтому результат делим на 10
cycle5 = int(cycle5 / 10)
for i in range(N):
    orbits[i][2] = int(orbits[i][2] / 10)


# print(orbits)
# print(cycle3, cycle4, cycle5)
# print(cycle3_list)
