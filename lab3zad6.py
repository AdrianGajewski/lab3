import random


def deck():
    talia = []
    ranga = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'D', 'K', 'A')
    kolor = ('S', 'D', 'H', 'C')
    for x in ranga:
        for y in kolor:
            talia.append((x, y))
    print(talia)
    return talia


def shuffle_deck(deck):
    tasowanie = random.sample(range(0, 52), 52)
    potasowany = []
    for x in tasowanie:
        potasowany.append(deck.__getitem__(x))
    return potasowany


def deal(deck, n):
    podglad = []
    for x in range(n):
        karty = []
        for y in range(5):
            karty.insert(y, deck.pop(0))
            podglad.insert(x, karty)
    return podglad

print(deal(shuffle_deck(deck()),2))