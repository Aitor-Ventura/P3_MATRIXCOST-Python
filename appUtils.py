import sys, re

# @param input - fichero a procesar
# return matriz con el contenido del fichero y el coste dado en el mismo
def fromDataToMatrix(input):
    fich = open(input, "r")
    cont = fich.read()
    lines = cont.split('\n')
    first_line = lines[0].split()
    dimension1 = int(first_line[0])
    dimension2 = int(first_line[1])
    cost = int(first_line[2])
    
    matrix = []
    for row in lines[1::]: matrix.append([int(x) for x in row.split()])
    
    return matrix, cost, dimension1, dimension2

# Muestra el mensaje de ayuda y finaliza la ejecución
def displayHelp():
    print("""usage: main.py [-h] [-d [DIRECTORY] | -f [FILE]] [-p] [-t] [-sm | -st | -check]

    optional arguments:
        -h, --help                                  show this help message and exit
        -d [DIRECTORY], --directory [DIRECTORY]     process many files in a directory
        -f [FILE], --file [FILE]                    process a single file
        -dd, --dimension                            display square matrix dimension
        -c, --cost                                  display cost
        -p, --paths                                 display total paths that can be done with given cost
        -t, --time                                  display execution time
        -sm, --memoization                          count number of paths in a matrix with given cost to reach
                                                        destination cell through Memoization
        -st, --tabulation                           count number of paths in a matrix with given cost to reach
                                                        destination cell through Tabulation
        -check                                      check that the number of paths in a matrix with given cost
                                                        is the same through Tabulation and Memoization""")
    sys.exit()

# @param data - directorio
# return lista de elementos de un directorio ordenados alfanuméricamente
def sorted_alphanumeric(data):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ]
    return sorted(data, key=alphanum_key)

# @param argv - lista de argumentos
# @param s1, s2 - string que se comprueba si se encuentra en la lista
# return verdadero si se encuentra, falso si no
def contains(argv, s1, s2):
    return s1 in argv or s2 in argv

# @param argv - lista de argumentos
# @param s1, s2 - strings
# return índice en el que se encuentra s1 o s2 en argv
def indexOf(argv, s1, s2):
    if s1 in argv: return argv.index(s1)
    if s2 in argv: return argv.index(s2)