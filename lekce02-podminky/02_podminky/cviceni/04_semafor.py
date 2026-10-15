# Cvičení 4 – Podmínky
# Doplň kód pod zadání a soubor spusť (Run).

# Máš proměnnou barva se stavem semaforu ("červená", "oranžová"
#    nebo "zelená"). Vypiš, co má řidič udělat:
#    "červená" → "Stůj", "oranžová" → "Připrav se", "zelená" → "Jeď",
#    cokoli jiného → "Neznámý signál".
barva = "zelená"

if barva == "červená":
    print ("Stůj")
elif barva == "oranžová":
    print ("priprav se")
elif barva == "zelená":
    print ("jeď")
else:
    print ("chyba semaforu")


if a>= 0 and b >= 0:
    print ()

    a = - 1
    b = 5
    print not ((a>0 and b < 0))

heslo_ok = True
jmeno_ok = False

if not (heslo_ok and jmeno_ok):
    print ("prihlaseni neplatne")

