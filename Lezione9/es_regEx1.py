# Definire una RegEx che riconosca solo stringhe composte da cifre.

#     Esercizio 1.1: Scrivi una RegEx che riconosca un numero intero positivo (es. 123, 98765).
#     Esercizio 1.2: Modifica la RegEx per accettare anche numeri negativi (es. -45, -1000, 0).


import re

#esercizio 1.1
lst_num:str= "123, 98765"
n_int_pos:list[int] = re.findall(r'\d+', lst_num)
print(n_int_pos)

#esercizio 1.2
lst_num2:str = "-45, -1000, 0"
n_neg:list[int] = re.findall(r'-.\d+', lst_num2)
print(n_neg)

