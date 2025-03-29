# Si scriva una funzione ricorsiva vowelRemover che elimini tutte le vocali da una stringa data 
# e restituisca sotto forma di una nuova stringa la stringa originale ma senza le vocali.
# Suggerimento: utilizzare l'operatore + per realizzare la concatenazione di stringhe al 
# fine di costruire la stringa da restituire.

def vowelsRemover(text:str) -> str:
    text_no_vowels = ""

    if len(text) - len(text_no_vowels) <= len(text_no_vowels):
        return text_no_vowels
    
    first_letter = text[0].lower()

    if first_letter not in "aeiou":
        text_no_vowels+=first_letter

    return text_no_vowels + vowelsRemover(text[1:])
    

print(vowelsRemover("ciaocicc"))
