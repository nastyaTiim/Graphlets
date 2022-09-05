from itertools import permutations
import numpy as np


def G1_search(N, G, orbits):
    G1 = np.array([[0, 1, 0],
                   [1, 0, 1],
                   [0, 1, 0]])
    counter = 0
    for triple in permutations(range(N), 3):
        i = triple[0]
        j = triple[1]
        k = triple[2]
        if i > k:      # условие, чтобы не считать граф-путь дважды
            continue

        G_copy = np.copy(G)

        G_copy[:, [0, i]] = G_copy[:, [i, 0]]
        G_copy[:, [1, j]] = G_copy[:, [j, 1]]
        G_copy[:, [2, k]] = G_copy[:, [k, 2]]

        G_copy[[0, i]] = G_copy[[i, 0]]
        G_copy[[1, j]] = G_copy[[j, 1]]
        G_copy[[2, k]] = G_copy[[k, 2]]

        if np.array_equal(G_copy[0:3, 0:3], G1) and G[i][j] and G[j][k] and not G[i][k]:
            counter += 1
            orbits[i][0] += 1
            orbits[j][1] += 1
            orbits[k][0] += 1
    return counter


def G4_search(N, G, orbits):
    G4 = np.array([[0, 1, 0, 0],
                   [1, 0, 1, 1],
                   [0, 1, 0, 0],
                   [0, 1, 0, 0]])
    nodes = []
    counter = 0
    for four in permutations(range(N), 4):
        i = four[0]
        j = four[1]
        k = four[2]
        p = four[3]

        G_copy = np.copy(G)

        G_copy[:, [0, i]] = G_copy[:, [i, 0]]
        G_copy[:, [1, j]] = G_copy[:, [j, 1]]
        G_copy[:, [2, k]] = G_copy[:, [k, 2]]
        G_copy[:, [3, p]] = G_copy[:, [p, 3]]

        G_copy[[0, i]] = G_copy[[i, 0]]
        G_copy[[1, j]] = G_copy[[j, 1]]
        G_copy[[2, k]] = G_copy[[k, 2]]
        G_copy[[3, p]] = G_copy[[p, 3]]

        if np.array_equal(G_copy[0:4, 0:4], G4) and G[i][j] and G[k][j] and G[p][j] \
                and not G[i][k] and not G[i][p] and not G[k][p]:
            if sorted([i, j, k, p]) in nodes:
                continue
            counter += 1
            orbits[i][2] += 1
            orbits[j][3] += 1
            orbits[k][2] += 1
            orbits[p][2] += 1
            nodes.append(sorted([i, j, k, p]))
    return counter


N = 6
# G = np.array([[0, 1, 0, 0, 0],
#               [1, 0, 1, 0, 1],
#               [0, 1, 0, 0, 0],
#               [0, 0, 0, 0, 1],
#               [0, 1, 0, 1, 0]])

G = np.array([[0, 0, 1, 1, 0, 0],
              [0, 0, 0, 1, 0, 0],
              [1, 0, 0, 0, 1, 1],
              [1, 1, 0, 0, 0, 1],
              [0, 0, 1, 0, 0, 0],
              [0, 0, 1, 1, 0, 0]])

orbits = [[0 for i in range(4)] for j in range(N)]  # G[i][0] орбита 1
                                                    # G[i][1] орбита 2
                                                    # G[i][2] орбита 6
                                                    # G[i][3] орбита 7

#print(counter)
#print(orbits)
