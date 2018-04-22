from array import *
import random

def tab():
    try:
        tablica = ('i', [random.sample(range(-5, 5), 5)])
        with open('results.txt', 'a') as f:
            f.write("Elementy tablicy: \n ")
            f.write(str(tablica))
            f.write("\n")
    finally:
        return tablica
        f.close()

tab()
