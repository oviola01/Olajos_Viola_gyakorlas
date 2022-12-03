sorozat = [-3, 5, 11, -2, 4]

#szeparátoros feladat

def method(listam, separator = " "):
    i = 0
    kiiras = ""
    while i < len(listam)-1:
        kiiras += str(listam[i]) + str(separator)
        i += 1
    kiiras += str(listam[i])
    print(kiiras)

method(sorozat, input("Adj meg egy elválasztó jelet! "))

#másik feladat
"""elsőhöz hozzáadni egy véletlent, 5 és 12 közt legyen
utsó bekérős, páratlan, hárommal osztható, kétjegyű"""

import random

def bekeres(szam):
    while (szam < 10) or (szam >= 100) or (szam % 2 == 0) or (szam % 3 != 0):
        szam = int(input("Sajnos ez nem jó, kérlek adj meg egy másik számot!"))
    return szam

def keresem(lista):
    j = 0
    while lista[j] < 10 and j < len(lista)-1:
        j += 1
    print(f"Az első kétjegyű szám a sorozatban a {lista[j]}, ami a {j + 1}. elem.")

def prim(tomb):
    #ezzel még csinálni kell valamit, mert most semmire se jó
    k = 0
    darab = 0
    while k < len(tomb)-1:
        if tomb[k] :
            darab += 1
        k += 1
    print(f"Összesen {darab} prím szám van a sorozatomban.")

def modify():
    #1 első elem módosítása
    sorozat[0] += (int(random.random()*8)+5)
    #2 új utolsó elem hozzáadása
    sorozat.append(bekeres(int(input("Kérlek adj meg egy páratlan, hárommal osztható, kétjegyű számot!"))))
    #3 kiírás az előző metódussal, szóközzel, paraméter nélkül
    method(sorozat,)
    #4 első kétjegyű helye és értéke
    keresem(sorozat)
    #5 prímek száma
    prim(sorozat)

modify()