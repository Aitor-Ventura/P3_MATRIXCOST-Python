# O(m * n * cost)
import time
import numpy as np

# @param mat - matriz con todos los elementos
# @param cost - coste máximo para hallar el camino
def countPaths_Tabulation(mat, cost):
    startTime = time.time()
    tab = np.zeros((len(mat), len(mat[0]), cost + 1))
    # El coste no puede ser negativo
    if mat[0][0] > cost: totalPaths = 0
    tab[0][0][mat[0][0]] = 1

    sum = 0
    for i in range(0, len(mat)):
        sum += mat[i][0]
        if sum <= cost: tab[i][0][sum] = 1
    
    sum = 0
    for i in range(0, len(mat[0])):
        sum += mat[0][i]
        if sum <= cost: tab[0][i][sum] = 1

    # Tabulation
    for i in range(1, len(mat)):
        for j in range(1, len(mat[0])):
            for k in range(0, cost + 1):
                if k - mat[i][j] >= 0: tab[i][j][k] = tab[i - 1][j][k - mat[i][j]] + tab[i][j - 1][k - mat[i][j]]

    totalPaths = tab[len(mat) - 1][len(mat[0]) - 1][cost]

    elapsedTime = time.time() - startTime
    return totalPaths, format(elapsedTime, '.2f')