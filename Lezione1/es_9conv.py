#es 9 lez 1 flowcharts

# Progetta un algoritmo che forniti dall'utente 
# 20 totali di vendita e i nomi dei venditori, 
# trova i due nomi dei venditori con il totale 
# più alto e il totale più basso delle vendite.

nome:str = str(input("Inserisci il nome del venditore: "))
vendita:float = float(input("Inserisci quanto ha venduto: "))

cont = 0
max_nome = nome
max_vend = vendita
min_nome = nome
min_vend = vendita

while cont < 20:

    new_nome = str(input("Inserisci il nome del venditore: "))
    new_vend = float(input("Inserisci quanto ha venduto: "))

    if new_vend > max_vend:

        max_vend = new_vend
        max_nome = new_nome

    if new_vend < min_vend:

        min_vend = new_vend
        max_nome = new_nome

    cont +=1

print(f"{max_nome}: {max_vend}")
print(f"{min_nome}: {min_vend}")