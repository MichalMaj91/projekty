import msvcrt
import math
import csv
from os import system

def fibonacci():
    while True:
        try:
            n = int(input("Podaj do jakiej wartosci ciągu: "))
            break 
        except ValueError:
            print("podana wartość nie jest liczbą.")
    fn1 = 0
    fn2 = 1
    fibo = []
    if n == 0:
        print(0)
        do_pliku = 0
    elif n < 0 :
        do_pliku = ("brak elementów do wyswetlenia")
        print(do_pliku)
    else:
        fibo.append(fn1)
        while n >= fn2:
            fibo.append(fn2)
            print(fn2, end=",")
            fn1, fn2 = fn2, fn1 + fn2   
        for i in fibo:
            print(i, end=',')
    do_pliku = str(n) + "|" + str(fibo)
    print("\nNaciśnij dowolny klawisz by kontynuować.")
    msvcrt.getch()
    return do_pliku

def bmi():
    wzrost = float(input("Poadj swój wzrost (w metrach): "))
    waga = float(input("Podaj swoją wagę (w kilogramach): "))
    bmi = round(waga / wzrost**2, 2)
    print("Twoje BMI wynosi:", bmi)
    print('Naciśnij dowolny klawisz, aby kontynuować.')
    do_pliku = str(waga) + " | " + str(wzrost) + " | " + str(round(waga / wzrost**2, 2))
    msvcrt.getch() 
    return do_pliku

def procenty1():
    while True:
        try:
            liczba = int(input("Podaj liczbę: "))
            break
        except ValueError:
            print("Podana wartosć nie jest liczbą!")


    while True:
        try:
            procent = int(input("Podaj procent z liczby: "))
            if procent < 0 :
                print("Podana wartość nie może być ujemna!")
            else:
                break
        except ValueError:
            print("Podana wartość nie jest liczbą!")

    print(procent, "% z liczby", liczba, "to:", round(procent/100*liczba, 2) )
    print('Naciśnij dowolny klawisz, aby kontynuować.')
    do_pliku = str(procent) + " | " + str(liczba) + " | " + str(round(procent/100*liczba, 2) )
    msvcrt.getch() 
    return do_pliku

def procenty2():
    while True:
        try:
            liczba1 = int(input("Podaj pierwszą liczbę: "))
            break
        except ValueError:
            print("Podana wartość nie jest liczbą! ")

    while True:
        try:
            liczba2 = int(input("Podaj drugą liczbę: "))
            break
        except ValueError:
            print("Podana wartość nie jest liczbą! ")

    print("liczba", liczba1, "stanowi", round((liczba1/liczba2*100),2), "procent liczby", liczba2, ".")
    do_pliku = str(liczba1) + " | " + str(liczba2) + " | " + str(round((liczba1/liczba2*100),2))
    msvcrt.getch()
    return do_pliku

def stezenie():
    liczba_moli = float(input("Podaj liczbę moli: "))
    Objętość = float(input("Podaj objętość roztworu(dm3): "))
    print("stężenie molowe substancji wynosi", round(liczba_moli/Objętość, 2), "moli/dm3")
    print('Naciśnij dowolny klawisz, aby kontynuować.')
    do_pliku = str(liczba_moli) + "|" + str(Objętość) + "|" + str(round(liczba_moli/Objętość, 2))
    msvcrt.getch()
    return do_pliku

def kolo():
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
            msvcrt.getch
            break
        elif menu == "3":
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
                    break
            except FileNotFoundError:
                print("Nie znaleziono pliku.")
                print("Naciśnij dowolny klawisz, aby kontynuować.")
                msvcrt.getch()
        else :
            print("Podano nieprawidłową opcję.")
            print("Naciśnij dowolny klawisz, aby kontynuować.")
            msvcrt.getch()
    return do_pliku

def zapis(nazwa, do_pliku):
    with open(nazwa + ".txt", "a", encoding = "utf-8") as plik:
        plik.write(do_pliku + "\n")

