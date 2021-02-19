from appUtils import *
from tabulation import *
from memoization import *
from copy import deepcopy
import sys, os

# Variables de control
# argv argumentos pasados por la línea de órdenes
# tbF, mmF, checkF, booleanas que controlan el flujo de hacer tabulation
#   memoization, o check (ambas)
argv = sys.argv
tbF = mmF = checkF = False

# Printa por pantalla el resultado de las opciones pasadas por línea de órdenes
def printOptions():
    if contains(argv, "-dd", "--dimension"): print(str(dimension1)+"x"+str(dimension2), end = "\t")
    if contains(argv, "-c" , "--cost"     ): print(str(cost), end = " cost \t")
    if contains(argv, "-p" , "--paths"    ): print(str(int(totalPaths)), end=" paths \t")
    if contains(argv, "-t" , "--time"     ): print(str(tiempo), end ="s\t")
    print()

# Muestra el mensaje de ayuda
if contains(argv, "-h", "--help"): displayHelp()

# Control de metodología
if "-check" in argv:                         tbf, mmF, checkF = False, False, True
elif contains(argv, "-sm", "--memoization"): tbF, mmF, checkF = False, True , False
elif contains(argv, "-st", "--tabulation" ): tbF, mmF, checkF = True , False, False

# Declaración de variables para indicar si es un directorio o un fichero
# isDirectory self explanatory
# input variable que se procesará
isDirectory, input = False, None

# Se indica que es un directorio y se asigna input al directorio pasado por línea de órdenes
if (contains(argv, "-d", "--directory")): isDirectory, input = True, argv[indexOf(argv, "-d", "--directory") + 1]

# Se indica que es un fichero y se asigna input al fichero pasado por línea de órdenes
elif (contains(argv, "-f", "--file")):                 input =       argv[indexOf(argv, "-f", "--file")      + 1]

# Procesamiento de directorios
if isDirectory:
    # Se ordena alfanuméricamente (en vez de 1 10 100 2 20 200, 1 2 10 20 100 200) el contenido
    #   del directorio
    cont = sorted_alphanumeric(os.listdir(input))

    for fich in cont:
        matrix, cost, dimension1, dimension2 = fromDataToMatrix(input + "/" + fich)
        # Check - Se comprueba que el resultado por Tabulation y Memoization es el mismo
        if checkF:
            tabulation  = deepcopy(matrix)
            memoization = deepcopy(matrix)

            totalPaths, tiempo = countPaths_Tabulation(tabulation, cost)
            totalPathsTab = totalPaths

            totalPaths, tiempo = countPaths_Memoization(memoization, cost)
            totalPathsMem = totalPaths

            if totalPathsMem == totalPathsTab: 
                print("Check: True - Number of paths is the same through Tabulation and Memoization | ", input + "/" + fich, end = "\t")
                printOptions()
            else: print("[!!! ERROR !!!] Check: False - Number of paths is NOT the same through Tabulation and Memoization")

        # Tabulation - Se resuelve el problema por Tabulation
        elif tbF:
            tabulation = deepcopy(matrix)
            totalPaths, tiempo = countPaths_Tabulation(tabulation, cost)
            print("Tabulation:  ", input+"/"+fich, end = "\t")
            printOptions()

        # Memoization - Se resuelve el problema por Memoization
        elif mmF:
            memoization = deepcopy(matrix)
            totalPaths, tiempo = countPaths_Memoization(memoization, cost)
            print("Memoization: ", input+"/"+fich, end = "\t")
            printOptions()

# Procesamiento de ficheros
else:
    # Se asigna la matriz y el coste indicados en el fichero de entrada
    matrix, cost, dimension1, dimension2 = fromDataToMatrix(input)

    # Check - Se comprueba que el resultado por Tabulation y Memoization es el mismo
    if checkF:
        tabulation  = deepcopy(matrix)
        memoization = deepcopy(matrix)

        totalPaths, tiempo = countPaths_Tabulation(tabulation, cost)
        totalPathsTab = totalPaths

        totalPaths, tiempo = countPaths_Memoization(memoization, cost)
        totalPathsMem = totalPaths

        if totalPathsMem == totalPathsTab: 
            print("Check: True - Number of paths is the same through Tabulation and Memoization | ", input, end = "\t")
            printOptions()
        else: print("[!!! ERROR !!!] Check: False - Number of paths is NOT the same through Tabulation and Memoization")

    # Tabulation - Se resuelve el problema por Tabulation
    elif tbF:
        tabulation = deepcopy(matrix)
        totalPaths, tiempo = countPaths_Tabulation(tabulation, cost)
        print("Tabulation:  ", input, end = "\t")
        printOptions()

    # Memoization - Se resuelve el problema por Memoization
    elif mmF:
        memoization = deepcopy(matrix)
        totalPaths, tiempo = countPaths_Memoization(memoization, cost)
        print("Memoization: ", input, end = "\t")
        printOptions()