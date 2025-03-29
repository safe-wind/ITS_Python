# Una produttoria è definita come il prodotto di un certo numero n di fattori, 
# con n intero positivo. Sia Pi una produttoria definita come segue:
# Pi = (0 + 2) * (1 + 2) * (2 + 2) * ... * (2 + n).  

# Calcolare il valore della produttoria Pi se n = 7.

def produttoria(n:int, somma:int = 2) -> int:

    if n <= 0:
        return 0+ somma
    
    else:
        return (n+somma)*produttoria(n-1, somma)
    
print(produttoria(7))
