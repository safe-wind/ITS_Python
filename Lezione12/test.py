from catalogo_film import MovieCatalog

#inizializzare un oggetto della classe movie catalog

catalog:MovieCatalog = MovieCatalog()

#print(catalog)

catalog.add_movies("Steven Spielberg", ["Casper", "Ritorno al futuro"])

catalog.add_movies("Steven Spielberg", ["ET"])
catalog.add_movies("Quentin Tarantino", ["Pulp Fiction", "Kill Bill"])
catalog.remove_movie("Quentin Tarantino", "Pulp Fiction")
catalog.remove_movie("Quentin Tarantino", "Kill Bill")
print(catalog.list_directors())

print(catalog)

print(catalog.get_movies_by_director("Steven Spielberg"))