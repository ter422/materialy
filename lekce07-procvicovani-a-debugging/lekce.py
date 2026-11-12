blacklist = ("HEgerová", "Vlk")

prichozi = input("Jak se jmenujes?")

for host in hoste:
    if prichozi == host:
        print("Pojd dal", prichozi)

def kontrola(prichozi):
    if prichozi in hoste:
        print("Pojd dal", prichozi)
    elif prichozi in blacklist:
        print("zmiz, nez si te vsimne karel")
    else:
        print("nejsi zvan.")

kontrola(prichozi, hoste. blacklist)

def pozvi(jmeno, hoste):
    hoste.append(jmeno)

pozvi("vojta", hoste)
print(hoste)
hoste(5:5) = ("Tom")
print(hoste)
hoste(0)= "Martina"
print(hoste)

#pop, remove, split, join

print(organizator.split())
rozdelene_jmeno = organizator.split()(0)(0)
print(rozdelene_jmeno)

fronta = ("vojta","petra","oslik","shrek")

fronta.pop()
