#esercizio4_11

pizza_fav : list[str] = ["Norvegese", "Margherita", "Diavola"]

for i in pizza_fav:
    print(f"\nLa pizza preferita è: {i}")

friend_pizzas = pizza_fav.copy()

#print(friend_pizzas)

pizza_fav.append("Patate")

friend_pizzas.append("Funghi")

for ii in pizza_fav:

    print(f"\nLa pizza preferita è: {ii}")

for iii in pizza_fav:

    print(f"\nLa pizza preferita è {iii}")

print(pizza_fav)
print(friend_pizzas)

