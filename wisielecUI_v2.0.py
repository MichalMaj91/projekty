import tkinter as tk
from tkinter import messagebox as box
import random 

lista_hasel = []

plik = open("wisielec.txt", 'r', encoding="utf-8")
for linia in plik.readlines():
    lista_hasel.append(linia.strip())
plik.close()



ilosc_hasel_w_pliku = len(lista_hasel) -1
liczba_zyc = 6
czyja_tura = 1
punkty_gracz_1 = 0
punkty_gracz_2 = 0


def wieszanie():
    if liczba_zyc == 5:
        lbl_rysunek.config(image=wisielec_1)
    elif liczba_zyc == 4:
        lbl_rysunek.config(image=wisielec_2)
    elif liczba_zyc == 3:
        lbl_rysunek.config(image=wisielec_3)
    elif liczba_zyc == 2:
        lbl_rysunek.config(image=wisielec_4)
    elif liczba_zyc == 1:
        lbl_rysunek.config(image=wisielec_5)
    elif liczba_zyc == 0:
        lbl_rysunek.config(image=wisielec_6)

def znajdz_indexy(haslo, litera):
    indeksy = []
    for index, litera_w_slowie in enumerate(haslo):
        if litera == litera_w_slowie or str.upper(litera) == litera_w_slowie:
            indeksy.append(index)
    return indeksy

def kolejna_runda():
    global punkty_gracz_1, punkty_gracz_2
    rozpocznij()
    uzyte_litery = []
    uzyte_litery_string = str(uzyte_litery)
    lbl_uzyte.config(text=uzyte_litery_string)
    lbl_uzyte_cd.config(text=uzyte_litery_string)
    lbl_liczba_zyc.config(text='Liczba żyć: ' + str(liczba_zyc))
    

def sprawdz():
    global liczba_zyc,uzyte_litery, punkty_gracz_1, punkty_gracz_2, czyja_tura, nastepna_gra
    wieszanie()
    litera = ent_litera.get()
    ent_litera.delete(0, tk.END)
    
    if len(litera) != 1:
        box.showerror("Błąd", "Wpisz jedną literę!")
    else:
        try:
            uzyte_litery.index(litera)
            box.showerror("Błąd", "Litera była już użyta!")
            liczba_zyc -= 1
            wieszanie()
            lbl_liczba_zyc.config(text='liczba żyć: ' + str(liczba_zyc))
            
            if liczba_zyc == 0:
                box.showinfo("Przegrana!", "Koniec gry! \nSzukane hasło to: " + losowanie_hasla)
                lbl_uzyte.config(text='')
                liczba_zyc = 6
                czyja_tura *= -1
                lbl_liczba_zyc.config(text=liczba_zyc)
                btn_rozpocznij.config(text='Następna runda', command=kolejna_runda)
                
        except ValueError:
            uzyte_litery.append(litera)
            
            if len(uzyte_litery) > 12:
                lbl_uzyte.config(text=str(uzyte_litery[0:12]))
                lbl_uzyte_cd.config(text=str(uzyte_litery[12:]))
                
            znalezione_indexy = znajdz_indexy(losowanie_hasla, litera)
            
            if len(znalezione_indexy) == 0:
                box.showerror("Błąd", "Nie ma takiej litery.")
                liczba_zyc -= 1
                wieszanie()
                lbl_liczba_zyc.config(text='Liczba żyć: ' + str(liczba_zyc))
                
                if liczba_zyc == 0:
                    box.showinfo("Przegrana", "Koniec gry! \nSzukane hasło to: " + losowanie_hasla)
                    uzyte_litery = []
                    lbl_uzyte.config(text='')
                    liczba_zyc = 6
                    czyja_tura *= -1
                    wieszanie()
                    lbl_liczba_zyc.config(text='Liczba żyć: ' + str(liczba_zyc))
                    btn_rozpocznij.config(text='Następna runda', command=kolejna_runda)
                    
            else:
                for index in znalezione_indexy:
                    haslo_uzytkownika[index] = litera
                    
            if "".join(haslo_uzytkownika) == str.lower(losowanie_hasla):
                box.showinfo("Gratulacje!", "Punkt dla Ciebie!\nSzukane hasło to: "+ losowanie_hasla)
                if czyja_tura > 0 :
                    punkty_gracz_1 += 1
                elif czyja_tura < 0 :
                    punkty_gracz_2 += 1
                lbl_punkty.config(text="Punkty gracz 1: "+ str(punkty_gracz_1)+ "\nPunkty gracz 2: " + str(punkty_gracz_2))
                czyja_tura *= -1
                lbl_uzyte.config(text='')
                liczba_zyc = 6
                wieszanie()
                lbl_liczba_zyc.config(text='Liczba żyć: ' + str(liczba_zyc))
                btn_rozpocznij.config(text='Następna runda', command=kolejna_runda)
            if punkty_gracz_1 == 3 or punkty_gracz_2 == 3:
                nastepna_gra = box.askquestion("Wygrana", "Gratulacje, wygrałeś. Czy rozpocząć nową grę?", icon = "info")   
                if nastepna_gra == "yes":
                    rozpocznij()
                    uzyte_litery = []
                    uzyte_litery_string = str(uzyte_litery)
                    lbl_uzyte.config(text=uzyte_litery_string)
                    lbl_uzyte_cd.config(text=uzyte_litery_string)
                    lbl_liczba_zyc.config(text='Liczba żyć: ' + str(liczba_zyc))
                    uzyte_litery_string = str(uzyte_litery)
                    lbl_uzyte.config(text=uzyte_litery_string)
                    punkty_gracz_1 = 0
                    punkty_gracz_2 = 0
                    lbl_punkty.config(text="Punkty gracz 1: "+ str(punkty_gracz_1)+ "\nPunkty gracz 2: " + str(punkty_gracz_2))
                    
                else:
                    okno_glowne.destroy()
    if len(uzyte_litery) > 12:
                lbl_uzyte.config(text=str(uzyte_litery[0:12]))
                lbl_uzyte_cd.config(text=str(uzyte_litery[12:]))
    haslo_uzytkownika_string = "".join(haslo_uzytkownika)
    lbl_hasło.config(text=haslo_uzytkownika_string)        



def rozpocznij():
    global liczba_zyc, losowanie_hasla, uzyte_litery, haslo_uzytkownika, haslo_uzytkownika_string, punkty_gracz_1, punkty_gracz_2
    
    if czyja_tura > 0:
        box.showinfo("Obecnie gra", "Tura gracza numer 1")
    elif czyja_tura < 0:
        box.showinfo("Obecnie gra", "Tura gracza numer 2")
        
    losowanie_hasla = lista_hasel[random.randint(0, ilosc_hasel_w_pliku)]
    
    uzyte_litery = []
    
    haslo_uzytkownika = []
    
    lbl_rysunek.config(image = wisielec_0)
    
    for _ in losowanie_hasla:
        haslo_uzytkownika.append("_")
        
    znalezione_indexy = znajdz_indexy(losowanie_hasla, " ")
    for index in znalezione_indexy:
        haslo_uzytkownika[index] = " "
    
    znalezione_indexy = znajdz_indexy(losowanie_hasla, ",")
    if len(znalezione_indexy) != 0:
        for index in znalezione_indexy:
            haslo_uzytkownika[index] = ","
            
    haslo_uzytkownika_string = "".join(haslo_uzytkownika)
    
    lbl_hasło.config(text=haslo_uzytkownika_string)
    
    btn_rozpocznij.config(text="Sprawdź", command=sprawdz)

def wyjdz():
    zapytanie = box.askquestion("Wyjście", "Czy napewno chcesz zamknąć aplikację", icon = "warning" )
    
    if zapytanie == "yes":
        okno_glowne.destroy()
    else:
        box.showinfo("Powrót", "Powrócisz teraz do aplikacji.")

def druga_wersja():
    global wisielec_6
    pytanie = box.askquestion("Grafika HD", "Czy włączyć grafikę HD?", icon = "warning" )
    if pytanie == "yes":
        wisielec_6 = tk.PhotoImage(file= "6bis.png")
    elif pytanie == "no":
        wisielec_6 = tk.PhotoImage(file= "6.png")

okno_glowne = tk.Tk()
okno_glowne.title("Wisielec v2.0")
okno_glowne.minsize(width=550, height=300)
okno_glowne.resizable(True, True)

okno_glowne.bind("<Escape>", lambda e: btn_wyjdz.invoke())
okno_glowne.bind("<Return>", lambda e: btn_rozpocznij.invoke())

okno_glowne.columnconfigure(0, weight=2)
okno_glowne.columnconfigure(1, weight=2)

wisielec_0 = tk.PhotoImage(file = "0.png")
wisielec_1 = tk.PhotoImage(file = "1.png")
wisielec_2 = tk.PhotoImage(file = "2.png")
wisielec_3 = tk.PhotoImage(file = "3.png")
wisielec_4 = tk.PhotoImage(file = "4.png")
wisielec_5 = tk.PhotoImage(file = "5.png")
wisielec_6 = tk.PhotoImage(file = "6.png")

lbl_hasło = tk.Label(okno_glowne, text="PRZYSŁOWIE", font=("Arial", 20, "bold"))
lbl_hasło.grid(column=0, row=0, columnspan=2, sticky=tk.EW, padx=5, pady=5)

lbl_rysunek = tk.Label(okno_glowne, image=wisielec_6)
lbl_rysunek.grid(column=1, row=1, rowspan=5, sticky=tk.EW, padx=5, pady=5)

lbl_uzyte = tk.Label(okno_glowne, text="Użyte litery: ", font=("Segoe UI", 14, "bold"))
lbl_uzyte.grid(column=0, row=1, columnspan=2, sticky=tk.W, padx=5, pady=5)
lbl_uzyte_cd = tk.Label(okno_glowne, text="", font=("Segoe UI", 14, "bold"))
lbl_uzyte_cd.grid(column=0, row=2, columnspan=2, sticky=tk.W, padx=5, pady=5)

lbl_liczba_zyc = tk.Label(okno_glowne, text= "Liczba żyć: " + str(liczba_zyc))
lbl_liczba_zyc.grid(column=0, row=3, sticky=tk.W, padx=5, pady=5)

lbl_punkty = tk.Label(okno_glowne, text="Punkty gracz 1: "+ str(punkty_gracz_1)+ "\nPunkty gracz 2: " + str(punkty_gracz_2))
lbl_punkty.grid(column=0, row=3, sticky=tk.E, padx=5, pady=5)

lbl_litera = tk.Label(okno_glowne, text="Wpisz literę: ")
lbl_litera.grid(column=0, row=4, sticky=tk.W, padx=5, pady=5)

ent_litera = tk.Entry(okno_glowne)
ent_litera.grid(column=0, row=4, sticky=tk.E, padx=5, pady=5)

btn_rozpocznij = tk.Button(okno_glowne, text="Rozpocznij", command=rozpocznij)
btn_rozpocznij.grid(column=0, row=5, sticky=tk.E, padx=5, pady=5)
btn_rozpocznij.focus_set()

btn_18 = tk.Button(okno_glowne, text="hd", command=druga_wersja)
btn_18.grid(column=0, row=5, padx=5, pady=5)

btn_wyjdz = tk.Button(okno_glowne, text="Wyjdź", command=wyjdz)
btn_wyjdz.grid(column=0, row=5, sticky=tk.W, padx=25, pady=5)

lbl_credits = tk.Label(okno_glowne, text="Game by Michał")
lbl_credits.grid(row=6, padx=30, pady= 10)

lbl_credits_2 = tk.Label(okno_glowne, text="Graphic by Zenon")
lbl_credits_2.grid(column=1, row=6, padx=30, pady= 10)

lbl_credits_3 = tk.Label(okno_glowne, text='I może trochę Sebuniunio ;)', font=('Arial', 3))
lbl_credits_3.grid(column=1, row=7, padx=30, pady=0)

okno_glowne.mainloop()