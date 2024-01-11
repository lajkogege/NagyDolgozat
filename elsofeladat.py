def beker():
    szam_be:int=int(input("Kérek egy páros számot! "))
    while not (szam_be %2 ==0):
        szam_be:int = int(input("Ez nem páros! Pároos számot kérek!"))
    print(szam_be)

def beker2():
    index:int=1
    lista=[]
    while (index!=4):
        szam_be: int = int(input(f"Kérek az {index} páros számot! "))
        while not (szam_be %2==0 ):
            szam_be:int=int(input(f"Ez nem páros szám. Kérem a {index}. páros számot! "))
        if szam_be%2==0:
            print(szam_be)
            lista.append(szam_be)
        else:
            szam_be: int = int(input(f"Ez nem páros szám. Kérem a {index}. páros számot! "))
        index+=1
    return lista

def legkisebb(listam):
    legkisebb:int=0
    index:int=0
    for i in range (0, len(listam),1):
        if listam[i]<legkisebb:
            legkisebb == listam[i]
            index+=1
    print(f"{index}. lépésben adta meg a legkisebb számot, melynek értéke: {legkisebb}")




