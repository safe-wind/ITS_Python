#es6_3

top_command:dict = {
    ".items();" :  "Riguarda i dizionari. dict.items() ti permette di estrarre chiavi e valori",
    ".values()" : "Riguarda i dizionari. dict.values() ti permette di estrarre i valori" ,
    ".sort()" : "Riguarda solo le liste. list.sort(): riorganizza una lista in ordine ascendente; discendente con il parametro reverse=True o anche in base al parametro key=..." ,
    ".sorted()" : "sorted(list, dict, tuple) è più comodo se si vuole creare una nuova lista e comunque mantenere la lista con cui si sta lavorando." ,
    ".pop()" : "Riguarda le liste. list.pop(i): rimuove l'elemento che si trova in posizione i " ,
    ".insert()" : "Riguarda le liste. list.insert(i, x): il primo argomento (i) è l'indice ([0],[1]..) dove viene inserito l'elemento (x). ",
}

i=0
for (c, w) in top_command.items():

    i=i+1

    if True:
        print(f"{i}){c},\n- {w}")