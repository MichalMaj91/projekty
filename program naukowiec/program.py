import funkcje 
from os import system
from msvcrt import getch
from sys import exit

profesja = -1

while True:
    system("cls")
    print("""Wybierz profesję:
    1. Naukowiec.
    2. Inżynier.
    3. Zamknij aplikację.""")

    profesja = input("Wprowadź 1, 2 lub 3:")

    if profesja == "1":
        while True:
            system('cls')
            print("""Wybierz Program:
            1. Oblicz BMI.
            2. Oblicz procenty.
            3. Oblicz stężenie molowe.
            4. Wróć do poprzedniego menu.
            5. Zamknij aplikację.""")
            menu = input("Wpisz co chcesz zrobić (1,2,3,4,5)?")
            if menu == "1":
                funkcje.zapis("bmi", funkcje.bmi())
            elif menu == "2":
                while True:
                    system("cls")
                    print("""Wybierz funkcję:
            1. Oblicz procent z liczby.
            2. Oblicz ile procent jednej liczby jest druga. 
            3. Wróć do poprzedniego menu.
            4. Zamknij aplikcję.""")
                    menu_procenty = input("Wpisz 1, 2, 3 lub 4. ")
                    if menu_procenty == "1":
                        funkcje.zapis("procenty1", funkcje.procenty1())
                    elif menu_procenty == "2":
                        funkcje.zapis("procenty2", funkcje.procenty2())
                    elif menu_procenty == "3":
                        break
                    elif menu_procenty == "4":
                        exit(0)
                    else:
                        print("Wprowadzono nieprawidłową opcję. ")
                        print("Naciśnij dowolny klawisz, aby kontynuować. ")
                        getch()
            elif menu == "3":
                funkcje.zapis("stezenie_molowe", funkcje.stezenie())
            elif menu == "4":
                break
            elif menu == "5":
                exit(0)
    elif profesja == "2":
        while True:
            system("cls")
            print("""Wybierz co chcesz zrobić:
        1. Oblicz pole i obwód koła.
        2. Wypisz ciąg Fibonacciego
        3. Wróc do poprzedniego menu.
        4. Zamknij aplikację.""")
            menu2 = input("Wpisz 1, 2, 3 lub 4.")
            if menu2 == "1":
                funkcje.zapis("obwod-i-pole", funkcje.kolo())
            elif menu2 == "2":
                funkcje.zapis("fibonacci", funkcje.fibonacci())
            elif menu2 == "3":
                break
            elif menu2 == "4":
                exit(0)
            else:
                print("Wprowadzono nieprawidłową opcję.")
                print("Naciśnij dowolny klawisz, aby kontynuować.")
                getch()
    elif profesja == "3":
        break
    else: 
        print("Wprowadzono nieprawidłową opcję.")
        print("Naciśnij dowolny klawisz, aby kontynuować.")
        getch()

print("Koniec działania programu.")
print("Naciśnij dowolny klawisz by zamknąć.")
getch()