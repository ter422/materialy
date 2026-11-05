def cena_mhd(vek):
    print("pocitam cenu listku pro vek", vek)

    if vek<6:
        print("cena 0")
        return 0
    elif vek<18:
        print("39")
        return 39
    elif vek<65:
        print("Cena 50")
        return 50
    else:
        print("Cena 0!")
        return 0

zustatek_uctu = 100
cena_jizdenky = cena_mhd(7)
print("vysedlna cena je", cena_jizdenky)

zustatek_uctu = zustatek_uctu - cena_jizdenky


      

