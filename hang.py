import random
lygis = input("iveskite lygi:")
zodziu_sarasas = []
while lygis <= 2:
    lygis = input("iveskite lygi:")

failo_objektas = open("zodziu_sarasas.txt", "r")
for zodis in failo_objektas.readlines():
    zodzio_ilgis = zodis.__len__()
    if int(lygis) >= int(zodzio_ilgis):
        zodziu_sarasas.append(zodis.replace("\n", ""))

random_index =random.randint(0,zodziu_sarasas.__len__())
print random_index
zodis_kuri_spet = zodziu_sarasas[random_index]
for i in  zodziu_sarasas:
    print i
