from dottore import Dottore
from fattura import Fattura
from paziente import Paziente
from persona import *

# Creo due dottori validi
dottore_1 = Dottore("Mario", "Rossi", 45, "Cardiologo", 100.0)
dottore_2 = Dottore("Luigi", "Bianchi", 50, "Neurologo", 120.0)

# Creo le liste di pazienti
paziente_1 = Paziente("Anna", "Verdi", 30, "PZ001")
paziente_2 = Paziente("Giovanni", "Neri", 40, "PZ002")
paziente_3 = Paziente("Sara", "Blu", 25, "PZ003")
lista_pazienti_1 = [paziente_1, paziente_2, paziente_3]
lista_pazienti_2 = [Paziente("Marco", "Viola", 35, "PZ004")]

# I dottori si presentano
dottore_1.doctorGreet()
dottore_2.doctorGreet()

# Creo le fatture
fattura1 = Fattura(lista_pazienti_1, dottore_1)
fattura2 = Fattura(lista_pazienti_2, dottore_2)

# Stampo i salari iniziali
print(f"Salario Dottore1: {fattura1.getSalary()} euro!")
print(f"Salario Dottore2: {fattura2.getSalary()} euro!")

# Rimuovo un paziente dal dottore 1 e lo aggiungo al dottore 2
paziente_rimosso = lista_pazienti_1[0]
fattura1.removePatient(paziente_rimosso.getidCode())
fattura2.addPatient(paziente_rimosso)

# Stampo i salari aggiornati
print(f"Salario Dottore1: {fattura1.getSalary()} euro!")
print(f"Salario Dottore2: {fattura2.getSalary()} euro!")

# Guadagno totale ospedale
guadagno_totale = (fattura1.getSalary() or 0) + (fattura2.getSalary() or 0)
print(f"In totale, l'ospedale ha incassato: {guadagno_totale} euro!")