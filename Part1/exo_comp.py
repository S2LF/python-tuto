nombres1 = [1, 21, 5, 44, 4, 9 ,5, 83, 29, 31, 25, 38]
nombres_pairs = [i for i in nombres1 if i % 2 == 0]
print(nombres_pairs)

nombres2 = range(-10, 10)
nombres_positifs = [i for i in nombres2 if i >= 0]
print(nombres_positifs)

nombre3 = range(5)
nombres_double = [i * 2 for i in nombre3]
print(nombres_double)

nombres4 = range(10)
nombres_inverses = [i if i % 2 == 0 else -i for i in nombres4]
print(nombres_inverses)