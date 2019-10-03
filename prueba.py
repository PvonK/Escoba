import itertools

numbers = [(1, "o"), (2, "e"), (3, "k"), (7, "f")]

carta = 4

for i in range(1, len(numbers)+1):
    lista = list(itertools.combinations(numbers, i))
print(list(max(lista)))
        


