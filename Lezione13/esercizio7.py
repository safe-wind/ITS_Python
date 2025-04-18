# Una produttoria è definita come il prodotto di un certo numero n di fattori, con n intero positivo.
# Sia Pi3 una produttoria definita come segue:
# Pi3 = (1**3) * (2**3) * (3**3) * ... * (n**3)  
# Calcolare il valore della produttoria Pi3 se n = 5.
 
def produttoria(n:int, prodotto:int = 3) -> int:

    if n <= 0:
        return 1
    else:
        return (n*prodotto) * produttoria(n-1, prodotto)

print(produttoria(5))