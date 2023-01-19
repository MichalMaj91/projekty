import math
import csv
from os import system
import msvcrt

menu = 0

while True:
    menu = 0 
    system("cls")
    print("""Wybierz:
            1. Wpisz promień.
            2. Wczytaj promienie z plików csv.
            3. Cofnij.""")

    menu = input()

    if menu == "1":
        promien = int(input("Podaj promień: "))
        obwod = round(2 * math.pi * promien, 2)
        pole = round(math.pi * (promien**2), 2)
        print("Koło o promieniu", promien, "ma obwód:", obwod, "pole: ", pole)
        do_pliku = str(promien) + " | " + str(obwod) + " | " + str(pole)
        print("Naciśnij dowolny klawisz, aby kontynuować.")
        msvcrt.getch()
        break
    elif menu == "3":
        do_pliku = "przerwano działanie programu."
        break 
    elif menu == "2":
        while True:
            nazwa_pliku_csv =str.strip(input("Wpisz nazwę pliku csv: "))
            if len(nazwa_pliku_csv) == 0:
                print("Nazwa pliku nie może być pusta")
            else:
                nazwa_pliku_csv = nazwa_pliku_csv + ".csv"
                break
        lista_obwod = []
        lista_pole = []
        lista_promien = []
        try:
            with open(nazwa_pliku_csv, "r") as plik_csv:
                czytnik_csv = csv.DictReader(plik_csv, delimiter = ";")

                for wiersz in czytnik_csv:
                    lista_promien.append(int(wiersz["promień"]))
                    lista_obwod.append(round(2 * math.pi * int(wiersz["promień"]), 2))
                    lista_pole.append(round(math.pi * (int(wiersz["promień"]) ** 2),2 ))

                for i in range(len(lista_promien)):
                    print("Koło o promieniu", lista_promien[i], "Obwód:", lista_obwod[i], "Pole:", lista_pole[i])
                
                do_pliku = str(lista_promien) + " | " + str(lista_obwod) + " | " + str(lista_pole)
                print(do_pliku)
                print("Naciśnij dowolny klawisz, aby kontynuować.")
                msvcrt.getch()
        except FileNotFoundError:
            print("Nie znaleziono pliku.")
            print("Naciśnij dowolny klawisz, aby kontynuować.")
            msvcrt.getch()
            break
    else :
        print("Podano nieprawidłową opcję.")
        print("Naciśnij dowolny klawisz, aby kontynuować.")
        msvcrt.getch()
