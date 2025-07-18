from string import ascii_lowercase

# def caesar_cypher_decrypt(s: str, key: int) -> str:

#     lettere:str = ascii_lowercase
#     if key > 26:
#         key = key % 26
#     frase_nuova:str = ""
#     s = s.lower()
#     for i in range(len(s)):
#         if s[i] in lettere:
#             posiz = lettere.index(s[i])
#             posiz1 = (posiz - key) % 26
#             new_carat = lettere[posiz1]
#             frase_nuova += new_carat
#         else:
#             frase_nuova += s[i]

#     return frase_nuova

# def caesar_cypher_encrypt(s: str, key: int) -> str:

#     lettere:str = ascii_lowercase
#     if key > 26:
#         key = key % 26
#     frase_nuova:str = ""
#     s = s.lower()
#     for i in range(len(s)):
#         if s[i] in lettere:
#             posiz = lettere.index(s[i])
#             posiz1 = (posiz + key) % 26
#             new_carat = lettere[posiz1]
#             frase_nuova += new_carat
#         else:
#             frase_nuova += s[i]

#     return frase_nuova

def ces_encr(parola_frase:str, key:int)-> str:
    parola_frase = parola_frase.lower()
    key = key%26
    alfabeto = ascii_lowercase
    new_str = ""

    for el in parola_frase:
        
        i = alfabeto.index(el)
        new_i  = (alfabeto[i+key])
        new_str+=new_i
    
    return new_str

parola = "ciao"

print(ces_encr(parola, 3))


    
