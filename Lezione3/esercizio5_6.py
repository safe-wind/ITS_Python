#esercizio 5_6

age: int = int(input("inserisci l'etè: "))

if age < 2:
    print("BABY")

elif age >= 2 and age < 4:
    print("TODDLER")

elif age >= 4 and age < 13:
    print("KID")

elif age >= 13 and age < 20:
    print("TEENAGER")

elif age >= 20 and age < 65:
    print("ADULT")
else:
    print("ELDER")



