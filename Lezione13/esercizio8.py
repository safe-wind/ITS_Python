# Si scriva una funzione ricorsiva vowelsCounter che conti il numero di vocali in una stringa.
# Suggerimento: ogni volta che si effettua una chiamata ricorsiva, si utilizzi lo slicing per
# ottenere una nuova stringa formata dai caratteri compresi tra il secondo e l'ultimo della stringa originale.
# L'ultima chiamata ricorsiva avverrà quando la stringa non contiene caratteri.   

def vowelsCounter(text:str) -> int:

    if len(text) == 0:
        return 0
    
    first_letter = text[0].lower()
    cont = 0

    if first_letter in "aeiou":
        cont = 1
    
    return cont + vowelsCounter(text[1:])

print(vowelsCounter("Halo"))
 