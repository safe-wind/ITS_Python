#es3_10

#prendiamo in considerazione solo le montagne > 3000mt

montagne_it: list = [
    "Marmolada", 
    "Ortles",
    "Bernina",
    "Gran Paradiso",
    "Cervino",
    "Monte Rosa",
    "Monte Bianco"
    ]
#utilizzo funzione .pop() sull' ultimo e il penultimo
#                    elemento della lista
montagne_it.pop(-2)
montagne_it.pop(-1)

print(montagne_it)

#Li reinserisco: uno con .append() e uno con .insert()

montagne_it.append("Monte Bianco")
montagne_it.insert(4, "Monte Rosa")

print(montagne_it)

#sorted() & .sort()

print(sorted(montagne_it))
montagne_it.sort(reverse=True)
print(montagne_it)

del montagne_it[0]
print(montagne_it)

montagne_it.insert(0, "Ortles")

montagne_it.sort(reverse=False)
print(montagne_it)