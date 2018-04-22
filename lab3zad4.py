import numpy

def tabela():
    table = numpy.zeros((5, 5))
    print(table)
    table[0,:] = [2, 3, 4, 5, 6]
    for i in range(1, 5):
        for j in range(0, 5):
            table[i, j] = table[i-1, j] ** 2
    print(table)


tabela()



def tab():
    tablica = ([[2, 3, 4, 5, 6], [], [], [], []])
    for x in range(1, 5):
        for y in range(0, 5):
            tablica[x].append(0)

    for x in range(1, 5):
         for y in range(0, 5):
             tablica[x][y] = tablica[x-1][y] ** 2
    print(tablica)


tab()
