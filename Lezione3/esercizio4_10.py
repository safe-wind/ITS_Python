#es4_10

container: list[str] = ["chiave", "casco", "ruota", "ammortizzatore", "disco"]
container1 : list[str] = ["cavo", "bullone", "olio", "faro"]

container.extend(container1)

#print(container)

print(container[0:3])

print(container[3:6])

print(container[6:9])