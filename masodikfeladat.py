import random
def random():
    random_lista=[]
    for i in range(0,13,1):
        random_szam=random.random()
        random_lista.append(random_szam)
    print(f"2. a, A lista: ")
    for i in range (0,len(random_lista),1):
        if random_lista[i] == len(random_lista)-1:
            print(random_lista[i])
        else:
            print(random_lista[i], end=";")

    print(f"2. a, A lista: [{random_lista}]")
    return random_lista

def ketjyegyuek_szama(random_listam):
    ketjegyu_db:int=0
    for i in range (0, len(random_listam),1):
        if random_listam[i]<= (-10) or random_listam[i]<=10:
            ketjegyu_db+=1
    return ketjegyu_db
