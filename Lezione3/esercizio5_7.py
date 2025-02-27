

fav_fruits: list[str] = ["strawberry", "grape", "pear", "peach"]

check_fruits : str = str(input("Scegli un frutto da cercare nella lista: "))

if check_fruits in  fav_fruits:

    print(f"You really like {check_fruits}")


else:

    print("il frutto non è nella lista")
    fav_fruits.append(check_fruits)                    
