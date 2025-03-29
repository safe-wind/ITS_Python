# Si scriva una funzione ricorsiva charDuplicator che consenta di duplicare ogni carattere in una stringa
# e restituisca il risultato sotto forma di una nuova stringa.
# Ad esempio, se la stringa "libro" viene data in input a charDuplicator, 
# la funzione ricorsiva deve produrre in output la stringa "lliibbrroo".

def charDuplicator(text:str) -> str:
    new_text = ""

    if len(text) == len(new_text)*2:
        return new_text
    
    first_letter = (text[0]*2).lower()

    if first_letter:
        new_text+=first_letter

    return new_text + charDuplicator(text[1:])

print(charDuplicator("libro"))