import os
from time import sleep

czy_jest = 0 
lista_zakupow = []
czy_dodac_produkt = input("Czy chcesz dodać produkt do listy zakupów? (t/n): ")
print()

while czy_dodac_produkt == "t":
    czy_jest = 0
    do_kupienia = str.capitalize(str.strip(input("Wpisz nazwę produktu: ")))

    if len(lista_zakupow) == 0:
        lista_zakupow += [do_kupienia]
    else:
        for produkt in lista_zakupow:
            if do_kupienia == produkt:
                czy_jest = 1 
                # print("Podany artykuł znajduje się już na liście")
                break
        if czy_jest == 1: 
            print("Podnay produkt znajduje się już na liście!")
        else:
            lista_zakupow += [do_kupienia]

    print()
    print("Obecnie na liście znajdują się produkty: ")
    for produkt in lista_zakupow:
        print(chr(10024) + " " + produkt)
    print()
    czy_dodac_produkt = input("Czy chcesz dodać kolejny produkt do listy zakupów (t/n)")
    print()

czy_robisz_zakupy = input("Czy robisz zakupy? (t/n)")
print()

os.system("cls")

while czy_robisz_zakupy == "t":
    if len(lista_zakupow) > 0:
        print("Lista zakupów: ")
        for produkt in lista_zakupow:
            print(chr(10024) + " " + produkt)
        print()
        kupione = str.capitalize(str.strip(input("Kupiony produkt: ")))
        if kupione in lista_zakupow:
            lista_zakupow.pop(lista_zakupow.index(kupione))
        else:
            print("Wpisany produkt nie występuje na liście zakupów!")
            print()
        czy_robisz_zakupy = input("Czy nadal robisz zakupy? (t/n): ")
        os.system("cls")
        print()
    else:
        print("Kupiłeś już wszystkie produkty z listy: ")
        print()
        break

if len(lista_zakupow) == 0:
    print("Skończyłeś robić zakupy. Lista zakupów jest pusta.")
else:
    print("Zostało do kupienia: ")
    for produkt in lista_zakupow:
        print(chr(10024) + " " + produkt)

sleep(2)
input("Naciśnij Enter, by zakończyć.")