# Recurrencia
# path(m, n, cost) = path(m    , n - 1, cost - M[m][n])     if m == 0
#                  = path(m - 1, n    , cost - M[m][n])     if n == 0
#                  = path(m - 1, n    , cost - M[m][n])
#                  + path(m    , n - 1, cost - M[m][n])     
#
# path(0, 0, cost) = 1                                      if M[m][n] == cost
#                  = 0                                      
#
# O(m * n * cost)
import time

# @param mat - matriz con todos los elementos
# @param cost - coste máximo para hallar el camino
def countPaths_Memoization(mat, cost):
    startTime = time.time()
    # Declaración de diccionario
    lookup = {}

    # @param mat - matriz con todos los elementos
    # @param m - numero de filas
    # @param n - numero de columnas
    # @param cost - coste restante para hallar el camino
    # @param lookup - diccionario
    # @return numero de caminos para alcanzar celda (m, n)
    def _countPaths(mat, m, n, cost, lookup):
        # El coste no puede ser negativo
        if cost < 0: return 0
        # Si estamos en la primera celda (0, 0)
        if m == 0 and n == 0: return int(mat[0][0] - cost == 0) # 1 True, 0 False

        key = (m, n, cost)
        # Si no se ha calculado el sub-problema con anterioridad
        if key not in lookup:
            # Si estamos en la primera fila, solo podremos ir hacia la izquierda
            if   m == 0: lookup[key] = _countPaths(mat, 0    , n - 1, cost - mat[m][n], lookup)
            # Si estamos en la primera columna, solo podremos ir hacia arriba
            elif n == 0: lookup[key] = _countPaths(mat, m - 1, 0    , cost - mat[m][n], lookup)
            # Calcular numero de caminos posibles yendo en ambas direcciones
            else:        lookup[key] = _countPaths(mat, m - 1, n    , cost - mat[m][n], lookup) + \
                                       _countPaths(mat, m    , n - 1, cost - mat[m][n], lookup)
        # Retornar numero de caminos posibles para llegar a la celda (m, n)
        return lookup[key]

    # switch -p
    totalPaths = _countPaths(mat, len(mat) - 1, len(mat[0]) - 1, cost, lookup)
    # switch -t
    elapsedTime = time.time() - startTime
    return totalPaths, format(elapsedTime, '.2f')