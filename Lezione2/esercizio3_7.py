#es3_7

invited:list = ["Marco Zucchero", "Vladimiro", "Elon Muschio", "Jeff Baffo", "Ronald Trump", "Kim Jong", "Farrel 'n Buffet"]

for i in invited:

    print(f"{i} il tavolo per la cena non si libererà in tempo per la cena. Ci sarà posto solo per due")

'''
rimosso1: str= invited.pop(0)
print(f"{rimosso1} purtroppo la cena è stata rimandata")
'''

rimosso1 : str = invited.pop(0)
print(f"{rimosso1} purtroppo la cena è stata rimandata")
rimosso2 : str = invited.pop(0)
print(f"{rimosso2} purtroppo la cena è stata rimandata")
rimosso3 : str = invited.pop(0)
print(f"{rimosso3} purtroppo la cena è stata rimandata")
rimosso4 : str = invited.pop(0)
print(f"{rimosso4} purtroppo la cena è stata rimandata")
rimosso5 : str = invited.pop(0)
print(f"{rimosso5} purtroppo la cena è stata rimandata")
 
for i in invited:

    print(f"{i} il tavolo per la cena non si libererà in tempo per la cena. Ci sarà posto solo per due")


del invited[0]
del invited[0]
#print della lista vuota
print(invited)