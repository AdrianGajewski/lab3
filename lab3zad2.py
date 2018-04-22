from array import *

def tab():
    tablica = []
    n = int(input('Ile elementów ma mieć tablica: '))
    for i in range(0, n):
        x = input('Wpisz elementy tablicy: ')
        tablica.append(x)
    print(tablica)
    tablica.reverse()
    print(tablica)
    return tablica
tab()