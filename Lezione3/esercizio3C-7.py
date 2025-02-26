#esercizio 3c_7

cont_coin=0

cont_t=0
cont_c=0

while cont_coin < 8:

    scelta: str = str(input("Scegli T o C: ").capitalize())
    
    match scelta:

        case scelta if scelta=="T":
            print(f"Lancio {cont_coin}: {scelta}")
            cont_t+=1
    
        case scelta if scelta=="C":
            print(f"Lancio {cont_coin}: {scelta}")
            cont_c+=1
    
    cont_coin=cont_c+cont_t
    

cont_tPcntl= (cont_t*100)//8
cont_cPcntl= (cont_c*100)//8

print(f"Lancio testa: {cont_t}.\n Percentuale: {cont_tPcntl:.2f}")
print(f"Lancio croce: {cont_c}.\n Percentuale: {cont_cPcntl:.2f}")


