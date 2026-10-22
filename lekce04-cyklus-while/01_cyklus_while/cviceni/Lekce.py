# while heslo != "pyladies":
#    print ("Nepřihlášena")
# print ("Vítej")

from random import randrange

hod = randrange(1,7)
while hod != 6:
      print("Padlo", hod, "hazime znovu")
      hod = randrange(1,7)
print("Padlo", hod, "vyhrala si")

while 1 == 2:
      print("ahoj")

soucet = 0
while True:
      odpoved = input("Zadej cislo ("nebo konec")")
      if odpoved == "konec:"
        break
    cislo = int(odpoved)
    if odpoved < 0:
     print("zaporna cisla ignorujeme")
     continue
    soucet = soucet + cislo
    print("zatim mame", soucet)
print("soucet", soucet)
     

