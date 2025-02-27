#es5_3

alien_green = "green"
alien_red = "red"
alien_yellow = "yellow"

points = 0

scelta: str = str(input("Inserisci un alieno da colpire: "))

if scelta == "green":
    points += 5
    print(f"{points:+}")
else:
    print(points)