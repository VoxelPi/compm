from functools import reduce

def list_to_sentence(list):
    return reduce(lambda sentence, word: f"{sentence} {word}", map(lambda word : "".join(word), list))

print(list_to_sentence([['i'], ['l', 'i', 'k', 'e'], ['c', 'a', 'k', 'e']]))

def harmonic_series(n):
    return reduce(lambda x, y: x + y, map(lambda x: 1/x, range(1, n+1)))

print(harmonic_series(100))