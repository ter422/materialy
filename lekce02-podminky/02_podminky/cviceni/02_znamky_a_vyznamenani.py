# Cvičení 2 – Podmínky
# Doplň kód pod zadání a soubor spusť (Run).

# Vrať se ke studentce se třemi známkami. Spočítej průměr a vypiš
#    "Máš vyznamenání!", když je průměr menší nebo rovný 2,
#    jinak vypiš "Bez vyznamenání.".
znamka1 = 1
znamka2 = 3
znamka3 = 2




print ("Hello world")
print (42)

#if podminka:
#    prikaz kdyz podminka plati

vek = int(input("Kolik je ti let? "))
if vek >= 18:
    print ("Jsi plnoletá.")

print ("konec programu")


znamka = 2
if znamka == 1:
    print ("Výborně")
elif znamka == 2:
    print ("Chvalitebně")
else:
    print ("To není platná známka.")

venku_prsi = True
mam_destnik = False
if venku_prsi:
    if mam_destnik:
        print ("co se dá delat, aspon ze nezmoknu")
    else:
        print ("to je teda smula, zmoknu")
else:
    if mam_destnik:
        print ("tahnu destnik zbytecne")
     