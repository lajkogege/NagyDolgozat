from Osztaly import Osztaly
def fajlbeolvas():
    fajl=open("stadionok.txt", "r", encoding="utf-8")
    fajl.readline()
    fajbol_sorok_lista=fajl.readlines()
    fajl.close()

    osztaly_lista=[]
    for i in range(0,len(fajbol_sorok_lista),1):
        aktelem=fajbol_sorok_lista[i]
        sor_lista=aktelem.strip().split(";")
        osztalyom=Osztaly(str(sor_lista[0]), str(sor_lista[1]), int(sor_lista[2]), str(sor_lista[3]), str(sor_lista[4]))
        osztaly_lista.append(osztalyom)
        return osztaly_lista


def csapat_darab(osztaly_listam):
    print(f"{len(osztaly_listam)} db csapat van.")

def newyork():
    for i in range()