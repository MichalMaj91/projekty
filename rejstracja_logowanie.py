import csv
import tkinter as tk  
from tkinter import ttk
import tkinter.messagebox as box
from math import pi
from tkinter import filedialog

lista_uzytkownikow = []
login_haslo = {}

with open("uzytkownicy.csv", "r", encoding="utf-8") as csv_uzytkownicy:
    csv_czytnik = csv.DictReader(csv_uzytkownicy, delimiter=";")
    
    for wiersz in csv_czytnik:
        login_haslo[wiersz["uzytkownik"]] = (wiersz["haslo"], wiersz["zawod"])

def wczytaj_dane():
    plik = filedialog.askopenfile(mode="r", filetypes=[("Pliki tekstowe", "txt")])
    if plik:
        zawartosc = plik.readlines()
        plik.close()
        zmienna_str = ''
        for i in range (len(zawartosc)):
            r = int(zawartosc[i].strip())
            obwod = round(2 * pi * r, 2)
            pole = round(pi * (r**2), 2)
            zmienna_str += 'Obwód:' + str(obwod) + ' Pole: ' + str(pole) +'\n'
        box.showinfo('Wyniki', zmienna_str)

def oblicz_pole_i_obwod():
    promien = int(ent_promien.get())
    obwod = round(2 * pi * promien, 2)
    pole = round(pi * (promien**2), 2)
    box.showinfo("Wyniki:", "Koło o promieniu " + str(promien) + " ma obwód: " + str(obwod) + " pole: " + str(pole))

def wypisz_ciag():
    wartosc = int(ent_wartosc.get())
    fn1 = 0
    fn2 = 1
    fibo = []
    if wartosc == 0:
        box.showwarning("Ostrzeżenie", "Brak elementów do wyświetlenia")
    elif wartosc < 0 :
        box.showerror("Błąd", "brak elementów do wyswetlenia")
    else:
        fibo.append(fn1)
        while wartosc >= fn2:
            fibo.append(fn2)
            print(fn2, end=",")
            fn1, fn2 = fn2, fn1 + fn2
        box.showinfo("Ciąg Fibonacciego","Elementy do wyświetlenia:" + str(fibo))

def oblicz_stezenie():
    mol = float(ent_liczba_moli.get())
    objetosc = float(ent_objetosc.get())
    wynik = round(mol/objetosc, 2)
    box.showinfo("Wynik" "stężenie molowe substancji wynosi" + str(wynik) + "moli/dm3")

def oblicz_bmi():
    wzrost = float(ent_wzrost.get())
    waga = float(ent_waga.get())
    bmi = round(waga / wzrost**2, 2)
    box.showinfo("BMI", "Twoje BMI wynosi: " + str(bmi))    

def oblicz_procent_1():
    liczba = ent_liczba_1.get()
    procent = int(ent_procent_1.get())
    try:
        liczba = int(ent_liczba_1.get())
    except ValueError:
        box.showerror("Podana wartosć jest nieprawidłowa!")
    if procent < 0:
        box.showerror("Podana wartość jest nieprawidłowa!")
    else:
        wynik = round(int(procent)/100*int(liczba), 2)
        box.showinfo("Wynik ", str(procent) + " % z liczby " + str(liczba) + " to: " + str(wynik))  

def oblicz_procent_2():
    liczba_a = ent_liczba_a.get()
    liczba_b = ent_liczba_b.get()
    try:
        liczba_a = int(ent_liczba_a.get())
        liczba_b = int(ent_liczba_b.get())
    except ValueError:
        box.showerror("Błąd", "Podano nieprawidłową wartosć.")
    wynik = round((int(liczba_a)/int(liczba_b)*100),2)
    box.showinfo("Wynik", "liczba" + str(liczba_a) + "stanowi" + str(wynik) +"procent liczby" + str(liczba_b) + ".")


def procenty_1():
    global ent_liczba_1, ent_procent_1
    okno_procenty_1 = tk.Tk()
    okno_procenty_1.title("Obliczanie procentu z liczby")
    okno_procenty_1.geometry("280x120")
    
    okno_procenty_1.columnconfigure(0, weight=2)
    okno_procenty_1.columnconfigure(1, weight=2)
    
    lbl_procent = tk.Label(okno_procenty_1, text="Podaj procent:")
    ent_procent_1 = tk.Entry(okno_procenty_1)
    
    lbl_liczba = tk.Label(okno_procenty_1, text="Podaj Liczbę:")
    ent_liczba_1 = tk.Entry(okno_procenty_1)
    
    btn_oblicz = tk.Button(okno_procenty_1, text="Oblicz", command=oblicz_procent_1)
    
    lbl_procent.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)
    ent_procent_1.grid(column=1, row=0, sticky=tk.W, padx=5, pady=5)
    lbl_liczba.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)
    ent_liczba_1.grid(column=1, row=1, sticky=tk.W, padx=5, pady=5)
    btn_oblicz.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)

def procenty_2():
    global ent_liczba_a, ent_liczba_b
    okno_procenty_2 = tk.Tk()
    okno_procenty_2.title("Obliczanie ile procent jednej liczby stanowi druga liczba")
    okno_procenty_2.geometry("320x140")
    
    okno_procenty_2.columnconfigure(0, weight=2)
    okno_procenty_2.columnconfigure(1, weight=2)
    
    lbl_liczba_a = tk.Label(okno_procenty_2, text="Podaj pierwszą liczbę:")
    ent_liczba_a = tk.Entry(okno_procenty_2)
    
    lbl_liczba_b = tk.Label(okno_procenty_2, text="Podaj drugą liczbę:")
    ent_liczba_b = tk.Entry(okno_procenty_2)
    
    btn_oblicz = tk.Button(okno_procenty_2, text="Oblicz", command=oblicz_procent_2)
    
    lbl_liczba_a.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)
    ent_liczba_a.grid(column=1, row=0, sticky=tk.W, padx=5, pady=5)
    lbl_liczba_b.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)
    ent_liczba_b.grid(column=1, row=1, sticky=tk.W, padx=5, pady=5)
    
    btn_oblicz.grid(column=1, row= 3, sticky=tk.E, padx=5, pady=5)

def wybor_procenty():
    if lb_wybor_dzialania.curselection()[0] == 0:
        procenty_1()
    elif lb_wybor_dzialania.curselection()[0] == 1:
        procenty_2()
    else:
        box.showwarning("Błąd", "Wybierz odpowiednie działanie.")

def procenty():
    global lb_wybor_dzialania
    okno_procenty = tk.Tk()
    okno_procenty.title("Działania na procentach.")
    okno_procenty.geometry("240x150")
    
    okno_procenty.columnconfigure(0, weight=2)
    okno_procenty.columnconfigure(1, weight=2)
    
    
    lb_wybor_dzialania = tk.Listbox(okno_procenty, selectmode=tk.SINGLE, width=30, height=4)
    lb_wybor_dzialania.insert(1, "1. Procenty1")
    lb_wybor_dzialania.insert(2, "2. Procenty2")
    
    btn_wybor = tk.Button(okno_procenty, text="Dalej", command=wybor_procenty)
    
    lb_wybor_dzialania.grid(column=0, row=0, columnspan=2, sticky=tk.W, padx=5, pady=5)
    btn_wybor.grid(column=1, row=2, sticky=tk.E, padx=5, pady=5)
    

def bmi():
    global ent_wzrost, ent_waga
    okno_bmi = tk.Tk()
    okno_bmi.title("Obliczanie BMI.")
    okno_bmi.geometry("240x120")
    
    okno_bmi.columnconfigure(0, weight=2)
    okno_bmi.columnconfigure(1, weight=2)
    
    lbl_wzrost = tk.Label(okno_bmi, text="Podaj wzrost (m):")
    ent_wzrost = tk.Entry(okno_bmi)
    
    lbl_waga = tk.Label(okno_bmi, text="Podaj wagę (kg):")
    ent_waga = tk.Entry(okno_bmi)
    
    btn_oblicz = tk.Button(okno_bmi, text="Oblicz", command=oblicz_bmi)
    
    lbl_wzrost.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)
    ent_wzrost.grid(column=1, row=0, sticky=tk.W, padx=5, pady=5)
    
    lbl_waga.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)
    ent_waga.grid(column=1, row=1, sticky=tk.W, padx=5, pady=5)
    
    btn_oblicz.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)

def stezenie_molowe():
    global ent_liczba_moli, ent_objetosc
    okno_stezenie = tk.Tk()
    okno_stezenie.title("Obliczanie steżenia molowego.")
    okno_stezenie.geometry("320x120")
    
    okno_stezenie.columnconfigure(0, weight=2)
    okno_stezenie.columnconfigure(1, weight=2)
    
    lbl_liczba_moli = tk.Label(okno_stezenie, text="Podaj liczbę moli:")
    ent_liczba_moli = tk.Entry(okno_stezenie)
    
    lbl_objetosc = tk.Label(okno_stezenie, text="Podaj objętość roztworu (dm3):")
    ent_objetosc = tk.Entry(okno_stezenie)
    
    btn_oblicz = tk.Button(okno_stezenie, text="Oblicz", command=oblicz_stezenie)
    
    lbl_liczba_moli.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)
    ent_liczba_moli.grid(column=1, row=0, sticky=tk.W, padx=5, pady=5)
    
    lbl_objetosc.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)
    ent_objetosc.grid(column=1, row=1, sticky=tk.W, padx=5, pady=5)
    
    btn_oblicz.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)

def fibonacci():
    global ent_wartosc
    okno_fib = tk.Tk()
    okno_fib.title("Ciąg Fibonacciego")
    okno_fib.geometry("270x100")
    
    okno_fib.columnconfigure(0, weight=3)
    okno_fib.columnconfigure(1, weight=1)
    
    lbl_wartosc = tk.Label(okno_fib, text="""Podaj do jakiej wartości
                wypisać ciąg: """)
    ent_wartosc = tk.Entry(okno_fib)
    
    btn_wypisz = tk.Button(okno_fib, text="Wypisz wartości.", command=wypisz_ciag)
    
    lbl_wartosc.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)
    ent_wartosc.grid(column=1, row=0, sticky=tk.W, padx=5, pady=5)
    
    btn_wypisz.grid(column=1, row= 2, sticky=tk.E, padx=5, pady=5)

def pole_i_obwod():
    global ent_promien
    okno_pole_i_obwod = tk.Tk()
    okno_pole_i_obwod.title("Obliczanie pola oraz obwodu koła.")
    okno_pole_i_obwod.geometry("260x100")
    
    okno_pole_i_obwod.columnconfigure(0, weight=3)
    okno_pole_i_obwod.columnconfigure(1, weight=1)
    
    lbl_promien = tk.Label(okno_pole_i_obwod, text="Podaj promień okręgu:")
    ent_promien = tk.Entry(okno_pole_i_obwod)
    
    btn_oblicz = tk.Button(okno_pole_i_obwod, text="Oblicz", command=oblicz_pole_i_obwod)
    btn_wczytaj = tk.Button(okno_pole_i_obwod, text="Wczytaj dane", command=wczytaj_dane)
    
    lbl_promien.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)
    ent_promien.grid(column=1, row=0, sticky=tk.W, padx=5, pady=5)

    btn_oblicz.grid(column=1, row=2, sticky=tk.E, padx=5, pady=5)
    btn_wczytaj.grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)


def wybor_zadania():
    if zawod == "Naukowiec":
        try:
            if lb_wybor_zadania.curselection()[0] == 0:
                procenty()
            elif lb_wybor_zadania.curselection()[0] == 1:
                bmi()
            elif lb_wybor_zadania.curselection()[0] == 2:
                stezenie_molowe()
            elif lb_wybor_zadania.curselection()[0] == 3:
                okno_wyboru.destroy()
        except IndexError:
            box.showerror("Błąd", "Wybierz odpowiednie działanie")
    elif zawod == "Inżynier":
        try:
            if lb_wybor_zadania.curselection()[0] == 0:
                fibonacci()
            elif lb_wybor_zadania.curselection()[0] == 1:
                pole_i_obwod()
            elif lb_wybor_zadania.curselection()[0] == 2:
                okno_wyboru.destroy()
        except IndexError:
            box.showerror("Błąd", "Wybierz odpowiednie działanie")

def zaloguj():
    global lb_wybor_zadania, okno_wyboru, zawod
    user = ent_nazwa2.get()
    haslo = ent_haslo22.get()
    if user in login_haslo.keys():
        haslo_i_zawod = login_haslo.get(user)
        haslo_z_listy = haslo_i_zawod[0]
        zawod = haslo_i_zawod[1]
        if haslo_z_listy == haslo:
            okno_logowania.destroy()  
            okno_wyboru = tk.Tk()
            okno_wyboru.title("okno wyboru zadania.")
            okno_wyboru.geometry("240x150")
            lb_wybor_zadania = tk.Listbox(okno_wyboru, selectmode=tk.SINGLE, width=30, height=4)
            btn_dalej_2 = tk.Button(okno_wyboru, text="Dalej", command=wybor_zadania)
            btn_dalej_2.place(relx=0.7, rely=0.7)
            lb_wybor_zadania.pack()
            
            if zawod == "Naukowiec":
                    lb_wybor_zadania.insert(1, "1.Działania na procentach.")
                    lb_wybor_zadania.insert(2, "2.Obliczanie BMI.")
                    lb_wybor_zadania.insert(3, "3.Obliczanie stężenia molowego.")
                    lb_wybor_zadania.insert(4, "4.Zamknij.")
            elif zawod == "Inżynier":
                    lb_wybor_zadania.insert(1, "1.Wypisz ciąg Fibonacciego.")
                    lb_wybor_zadania.insert(2, "2.Oblicz pole i obwód koła.")
                    lb_wybor_zadania.insert(3, "3.Zamknij")
            lb_wybor_zadania.pack()
            
        else:
            box.showerror("Błąd", "Hasło niepoprawne.")
    else:
        box.showerror("Błąd", "Niepoprawny login.")

def rejestracja():
    global login_haslo
    
    user = str.strip(str.lower(ent_nazwa.get()))
    haslo = ent_haslo.get()
    haslo2 = ent_haslo2.get()
    zawod = wybor_1.get()
    
    if user in lista_uzytkownikow:
        box.showwarning("Ostrzeżenie" , "Podana nazwa już istnieje.")
    elif len(user) == 0 :
        box.showerror("Błąd", "Podana nazwa jest za krótka.")
    elif len(haslo) == 0:
        box.showerror("Błąd", "Podane hasło jest za krótkie.")
    elif haslo != haslo2:
        box.showerror("Błąd", "Podane hasła są różne.")
    else:
        login_haslo[user] = haslo 
        lista_uzytkownikow.append(user)
        ent_nazwa.delete(0, tk.END)
        ent_haslo.delete(0, tk.END)
        ent_haslo2.delete(0, tk.END)
        
        with open("uzytkownicy.csv", "a", encoding="utf-8") as do_pliku_csv:
            csv_zapis = csv.writer(do_pliku_csv, delimiter=";")
            csv_zapis.writerow([user, haslo, zawod])
        login_haslo = {}
        with open("uzytkownicy.csv", "r", encoding="utf-8") as csv_uzytkownicy:
            csv_czytnik = csv.DictReader(csv_uzytkownicy, delimiter=";")
            for wiersz in csv_czytnik:
                login_haslo[wiersz["uzytkownik"]] = (wiersz["haslo"], wiersz["zawod"])
    okno_rejestracji.destroy()

def anuluj():
    okno_rejestracji.destroy()

def zarejstruj():
    global ent_nazwa, ent_haslo, okno_rejestracji, ent_haslo2, wybor_1
    okno_rejestracji = tk.Tk()
    okno_rejestracji.geometry("280x200")
    okno_rejestracji.resizable(True, True)
    okno_rejestracji.title("Tworzenie nowego konta.")

    okno_rejestracji.columnconfigure(0, weight= 1)
    okno_rejestracji.columnconfigure(1, weight= 3)

    lbl_nazwa = ttk.Label(okno_rejestracji, text="Nazwa użytkownika:")
    lbl_nazwa.grid(column=0, row=1, sticky=tk.E, padx=5, pady=5)
    ent_nazwa = ttk.Entry(okno_rejestracji)
    ent_nazwa.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)

    wybor_1 = tk.StringVar(okno_rejestracji)
    wybor_1.set("Wybierz zawód dla którego\nchcesz wykonać zadanie:")
    menu_wyboru_1 = tk.OptionMenu(okno_rejestracji, wybor_1, "Naukowiec", "Inżynier")
    menu_wyboru_1.grid(column=0, row=4, columnspan=2, sticky=tk.E, padx=5, pady=5)

    lbl_haslo = ttk.Label(okno_rejestracji, text="Wpisz hasło:")
    lbl_haslo.grid(column=0, row=2, sticky=tk.E, padx=5, pady= 5)
    ent_haslo = ttk.Entry(okno_rejestracji, show="*")
    ent_haslo.grid(column=1, row=2, sticky=tk.E, padx=5, pady=5 )

    lbl_haslo2 = ttk.Label(okno_rejestracji, text="Wpisz ponownie hasło:")
    lbl_haslo2.grid(column=0, row=3, sticky=tk.E, padx=5, pady= 5)
    ent_haslo2 = ttk.Entry(okno_rejestracji, show="*")
    ent_haslo2.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5 )

    btn_register = ttk.Button(okno_rejestracji, text="Anuluj.", command=anuluj)
    btn_register.grid(column=0, row=5, sticky=tk.SE, padx=5, pady=5)

    btn_login = ttk.Button(okno_rejestracji, text="Rejestracja", command=rejestracja)
    btn_login.grid(column=1, row=5, sticky=tk.SE, padx=5, pady=5)
    


okno_logowania = tk.Tk()
okno_logowania.geometry("340x130")
okno_logowania.title("Logowanie")
    
okno_logowania.columnconfigure(0, weight=2)
okno_logowania.columnconfigure(1, weight=2)
    
lbl_logowanie2 = ttk.Label(okno_logowania, text="Wpisz nazwę użytkownika i hasło, by zalogować:")
lbl_logowanie2.grid(column=0, row=0, sticky=tk.SE, padx=5, pady=5)
    
lbl_nazwa2 = ttk.Label(okno_logowania, text="Nazwa użytkownika:")
lbl_nazwa2.grid(column=0, row=1, sticky=tk.S, padx=5, pady=5)
ent_nazwa2 = ttk.Entry(okno_logowania)
ent_nazwa2.grid(column=1, row=1, sticky=tk.S, padx=5, pady=5)
    
lbl_haslo22 = ttk.Label(okno_logowania, text="Hasło:")
lbl_haslo22.grid(column=0, row=2, sticky=tk.S, padx=5, pady=5)
ent_haslo22 = ttk.Entry(okno_logowania, show="*")
ent_haslo22.grid(column=1, row=2, sticky=tk.S, padx=5, pady=5)

btn_zarejestruj = ttk.Button(okno_logowania, text="Zarejestruj", command=zarejstruj)    
btn_zarejestruj.grid(column=0, row=3,sticky=tk.S, padx=5, pady=5)

btn_zaloguj = ttk.Button(okno_logowania, text="Zaloguj", command=zaloguj)
btn_zaloguj.grid(column=1, row=3, sticky=tk.S, padx=5, pady=5)

okno_logowania.mainloop()
