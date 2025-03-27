# Si supponga di voler calcolare l'ammontare del denaro depositato 
# su un conto bancario ad interesse composto. Se m è la somma depositata sul conto, 
# la somma disponibile alla fine del mese sarà 1.005 volte m.
# Scrivere una funzione ricorsiva compoundInterest che calcoli la somma presente sul conto 
# dopo t mesi data una somma di partenza m.

def amountDeposit(m:float, t:int):

    if m == 0:
        return "No funds"
    if t == 0:
        return m
    else:
        i_comp = 1.005 * amountDeposit(m,t-1)

        return round(i_comp, 2)
        
print(amountDeposit(100,12))
