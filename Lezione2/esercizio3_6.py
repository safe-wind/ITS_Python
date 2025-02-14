#3_6
invited: list = ["Vladimiro" , "Elon Muschio", "Ronald Trump", "Kim Kong"]

location:str = "al mc donald's di Termini"

for i in invited:
    print(f"Gentilissimo {i} abbiamo trovato un tavolo più grande e si unirà altra gente alla cena")

invited.insert(0, "Marco Zucchero")
invited.insert(3, "Jeff Baffo")
invited.append("Farrel 'n Buffet")

#print(invited)

print("\nInvitati alla cena:\n ")

for i_agg in invited:

    print(f"{i_agg}, ha ricevuto un invito a cena {location}")

#print(invited)

