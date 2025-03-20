# dal file persona.py importa la classe persona

from persona import Persona

#creare un oggetto di tipo persona
mg:Persona  = Persona ("Marius", "Gidilica", 23)

print(mg)
print(mg.name)
print(mg.last_name)
print(mg.age)

from persona2 import Persona
#creo un oggetto mg di tipo persona

mg:Persona = Persona()

#richiamo la funzione displayData() 

mg.displayData()

#impostare il nome della persona mg

mg.setName("Marius")

mg.displayData()

#impostare cognome persona mg

mg.setLastName("Gidilica")

#impostare eta della persona mg

mg.setAge(23)
mg.displayData()

print(mg.getName(), mg.getLastName(), mg.getAge())



