
import json

# PATH:str = "test.json"
# mode:str = "r"

# with open(PATH, mode=mode) as file:

#     config: dict = json.load(file)

#     print(config)

# PATH:str = "test_1.json"
# mode:str = "w"

# with open(PATH, mode=mode) as file:
    
#     config:dict = {"nome":"2048",
#                    "versione":"1.0.2",
#                    "os":"16.0.1"}
    
#     json.dump(config, file, indent=4)

# es n 1 
# crea un file json usando i comandi touch e nano. leggete il file e stampane il valore
# PATH:str = "es_1.json"

# with open(PATH,mode="r") as file:

#     lettura = json.load(file)
#     print(lettura)
#es n2 
#

PATH2 = "es_2.json"

with open(PATH2,mode="w") as file:

    dizio1 = {
        "gi":"no",
        "si":"si"
    }

    json.dump(dizio1, file)

