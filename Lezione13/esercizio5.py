# Una progressione armonica è definita come il prodotto dei reciproci dei primi n numeri interi positivi,
# ovvero il risultato della moltiplicazione di 1 diviso ogni numero intero da 1 fino a n.
# Ad esempio, se n = 6, la progressione armonica A vale:
# A = 1/6 * 1/5 * 1/4 * 1/3 * 1/2 * 1 = 0.001389.

def armonicRecursion(n:int) -> float:

    if n <= 0:
        return 1
    else:
        return 1/n * armonicRecursion(n-1)

    
print(round(armonicRecursion(6), 6))