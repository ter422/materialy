def vypis_cisla_do_max_hodnoty(jmeno_volani, max_hodnota, ukaz_caru):
    for aktualni_cislo in range(1, max_hodnota):
        print (jmeno_volani+":"+str(aktualni_cislo))
    if ukaz_caru:
        print ("-"*30)

vypis_cisla_do_max_hodnoty("volani A", 10, True)
vypis_cisla_do_max_hodnoty("volani B", 100, True)
vypis_cisla_do_max_hodnoty("volani C", 1000, False)