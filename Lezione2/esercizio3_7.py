#es3_7

invited:list = ["Marco Zucchero", "Vladimiro", "Elon Muschio", "Jeff Baffo", "Ronald Trump", "Kim Jong", "Farrel 'n Buffet"]

for i in invited:

    print(f"{i} il tavolo per la cena non si libererà in tempo per la cena. Ci sarà posto solo per due")

invited.pop(0)
print(f"{invited[0]} purtroppo la cena è stata rimandata")
invited.pop(0)
print(f"{invited[0]} purtroppo la cena è stata rimandata")
invited.pop(0)
print(f"{invited[0]} purtroppo la cena è stata rimandata")
invited.pop(0)
print(f"{invited[0]} purtroppo la cena è stata rimandata")
invited.pop(0)
print(f"{invited[0]} purtroppo la cena è stata rimandata")

del invited[0]
del invited[0]
#print della lista vuota
print(invited)
