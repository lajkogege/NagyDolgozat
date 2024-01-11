import random
def random():
    print("2.a feladat")
    random_lista:int=[]
    for i in range(0,13,1):
        szam:int=int(random.randint(-90,150))
        random_lista.append(szam)
    for i in range (0,len(random_lista),1):
        if random_lista[i] == len(random_lista)-1:
            print(random_lista[i])
        else:
            print(random_lista[i], end=";")
    return random_lista

def ketjyegyuek_szama(random_listam):
    print("2.b feldat: ")
    ketjegyu_db:int=0
    for i in range (0, len(random_listam),1):
        if random_listam[i]<= (-10) or random_listam[i]<=10:
            ketjegyu_db+=1
    print(f"2.b A kétjegyű számok száma: {ketjegyu_db}")
    return ketjegyu_db

def paros_osszeg(random_listam):
    osszegparos:int=0
    db:int=0
    for i in range(0, len(random_listam),1):
        if random_listam[i]%2==0:
            osszegparos += random_listam[i]
            db+=1
    return osszegparos

def paratlan_osszege(random_listam):
    osszegparatlan:int=0
    for i in range (0,len(random_listam),1):
        if not(random_listam[i] %2==0):
            osszegparatlan+=random_listam[i]
    return osszegparatlan

def paros_vagy_paratlan(paros, paratlan):
    print("2.e feladat:")
    if paros > paratlan:
        print(f"A párosok összege {paros} > a páratlan összege {paratlan}")
    else:
        print(f"A párosok összege {paros} < a páratlan összege {paratlan}")
