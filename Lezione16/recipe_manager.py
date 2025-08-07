# Sviluppa un sistema per la gestione delle ricette in Python che permetta agli utenti di creare, modificare, e cercare ricette basate sugli ingredienti. Il sistema dovrà essere capace di gestire una collezione (dizionario) di ricette e i loro ingredienti.
# Classe:
# - RecipeManager:
#     Gestisce tutte le operazioni legate alle ricette.
#     Metodi:
#     - create_recipe(name, ingredients): Crea una nuova ricetta con il nome specificato e una lista di ingredienti. Restituisce un nuovo dizionario con la sola ricetta appena creata o un messaggio di errore se la ricetta esiste già.
#     - add_ingredient(recipe_name, ingredient): Aggiunge un ingrediente alla ricetta specificata. Restituisce la ricetta aggiornata o un messaggio di errore se l'ingrediente esiste già o la ricetta non esiste.
#     - remove_ingredient(recipe_name, ingredient): Rimuove un ingrediente dalla ricetta specificata. Restituisce la ricetta aggiornata o un messaggio di errore se l'ingrediente non è presente o la ricetta non esiste.
#     - update_ingredient(recipe_name, old_ingredient, new_ingredient): Sostituisce un ingrediente con un altro nella ricetta specificata. Restituisce la ricetta aggiornata o un messaggio di errore se l'ingrediente non è presente o la ricetta non esiste.
#     - list_recipes(): Elenca tutte le ricette esistenti.
#     - list_ingredients(recipe_name): Mostra gli ingredienti di una specifica ricetta. Restituisce un elenco di ingredienti o un messaggio di errore se la ricetta non esiste.
#     - search_recipe_by_ingredient(ingredient): Trova e restituisce tutte le ricette che contengono un determinato ingrediente. Restituisce un elenco di ricette o un messaggio di errore se nessuna ricetta contiene l'ingrediente.

class RecipeManager:

    collezione: dict #

    def __init__(self):
        self.collezione : dict  = {}
    
    def create_recipe(self, name:str, ingredients:list[str]):
        if name not in self.collezione.keys():
            self.collezione[name] = ingredients
        else:
            print("La ricetta esiste già")
        return self.collezione

    def add_ingredient(self,recipe_name:str,ingredient:str):
        if recipe_name not in self.collezione:
            print("La ricetta non esiste")
        elif ingredient in self.collezione[recipe_name]:
            print("L'ingrediente è gia nella ricetta")
        else:
            self.collezione[recipe_name].append(ingredient)
            return (recipe_name,self.collezione[recipe_name])
    
    def remove_ingredient(self,recipe_name,ingredient):
        if recipe_name not in self.collezione:
            print("La ricetta non esiste")
        elif ingredient not in self.collezione[recipe_name]:
            print("L'ingrediente non è nella ricetta")
        else:
            self.collezione[recipe_name].remove(ingredient)
            return (recipe_name,self.collezione[recipe_name])
    
    def list_recipes(self):
        for k in self.collezione.keys():
            print(f"-{k}")
    
    def update_ingredient(self, recipe_name, old_ingredient, new_ingredient):
        if recipe_name not in self.collezione.keys():
            print("La ricetta non esiste")
        elif old_ingredient not in self.collezione[recipe_name]:
            print("L'ingrediente non è nella ricetta")
        else:
            self.collezione[recipe_name].remove(old_ingredient)
            self.collezione[recipe_name].append(new_ingredient)
        print(recipe_name, self.collezione[recipe_name])

    def list_ingredients(self, recipe_name):

        if recipe_name not in self.collezione.keys():
            print("La ricetta non esiste")
            
        else:
            for k in self.collezione.keys():
                if k == recipe_name:
                    for el in self.collezione[recipe_name]:
                        print(f"-{el}")

    def search_recipe_by_ingredient(self, ingredient):
        for k in self.collezione.keys():
            if ingredient in self.collezione[k]:
                print(f"-{k}")
            else:
                print("Non esiste nessuna ricetta con questo ingrediente")


manager = RecipeManager()
print(manager.create_recipe("Pizza Margherita", ["Farina", "Acqua", "Lievito", "Pomodoro", "Mozzarella"]))
print(manager.add_ingredient("Pizza Margherita", "Basilico"))
print(manager.update_ingredient("Pizza Margherita", "Mozzarella", "Mozzarella di Bufala"))
print(manager.remove_ingredient("Pizza Margherita", "Acqua"))
print(manager.list_ingredients("Pizza Margherita"))

    

