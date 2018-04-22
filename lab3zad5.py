from collections import Counter


def zliczanie(document):
    file = open(document, 'r')
    c = Counter()
    for x in file:
        c += Counter(x)
    print(c)
    return c


zliczanie("document.txt")

