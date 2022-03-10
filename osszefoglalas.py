# 'változó' :: névvel rendelkező hivatkozás egy bizonyos memóriaterületre

# valtozo_neve: [valtozo_tipusa] = valtozo_erteke
# deklaráció aka. "létrehozás + elnevezés + memóriafoglalás" -> inicializálás aka. "értékadás" vagy a "memóriaterület feltöltése"
# pl:
from lib2to3.pgen2.token import CIRCUMFLEX


x: int = 10
# a tipus megjelölése a nyelv ducktype mivolta miatt 'opcionális'

# típusok:
egyesz_szam: int = 10
lebegopontos_szam: float = 20.5
karakterlanc: str = 'szoveg'
logikai: bool = True

# típusokon végezhető műveletek
# - az, hogy valami milyen típusú, az meghatározza, hogy milyen műveletek végezhetőek vele
# a műveletek meghívását/elvégzését ún. operátorokkal jelezzük

# numerikus típusokon a matematikai operátorok működnek a 'hagyományos' módon
# bizonyos operátorok szempontjából két különböző típus ún. 'típuskompatibilis' lehet egymással
# pl 2:int + 1.5:float -> float

# karakterláncokon végezhető legjellemzőbb művelet a konkatenáció (összefűzés), jele a +
# pl.: 10 + ' ' + 'kismalac' -> '10 kismalac'

# logikai operátorok:
# not, or, and

# 'valami' == 'valami más' -> bool (False)

# összehasonlító operátorok:
# matlogból ismerős dolgok:
# <, >, <=, >=, ==, != -> bool

# halmazműveletek:
# in, not in -> bool

# [elemi érték] in [kollekció] -> ha benne van az érték a kollekcióban, akkor True, egyébként False


# 'kollekciók' aka. 'összetett adatszerkezetek':
# Pythonban minden kollekció alapvetűen heterogén (több fajta típucú dolog is lehet ugyan abban a kollekcióban)
# mi ezzel a lehetőséggel nem éltünk, és 'homogén' kollekciókként használtuk őket -> azaz olyan összetett szerkezeteket alkottunk, aminek minden egyes eleme azonos típusú.
# egy konkrét kollekciótípus ismerete szükséges az alapvizsgán: a lista:
# lista_neve = [] <- 'üres, névvel rendelkező lista
# lista_neve = [lista_elem, lista_elem, lista_elem] <- statikusan feltöltött lista (olyan lista, aminek deklarációkor megadom az első N elemét)
# lista adott elemére a lista_neve + elem_helye párossal tudok hivatkozni:
# lista_neve[0] -> ez a lista 0-ás ún. indexű eleme:
# a legtöbb programozási nyelvben a nem-asszociatív kollekciók elemeinek indexelése ún. zero-based, azaz az elemek rendre a természetes számokat veszik fel, mint "helymeghatározó index" (0, 1, 2, 3, 4....)
# -> ebből két dolog következik:
# a kollekció utolsó értékkel rendelkező indexű helye az az ([adatszerkezet_hossza] - 1)
# a pythonos listák hossza nem predeterminált, hosszuk a program futása során folyxamatosan változhat

# programozási vezérlőszerkezetek:

# elágazás:
# if [feltétel] -> bool:
#   [kód, ami akkor fut le, ha a feltétel eredménye True]
# else:
#   [kód, ami akkor fut le, ha a feltétel eredménye False]

# akármennyi if + else egymásba ágyazható ->
# ha az else ág CSAK egy újabb feltételvizsgálatot tartalmazna, akkor az else + if összevonható :: elif [feltétel]:

# if [első feltétel]:
#   (kód, ha az első feltétel True)
# elif [másidik feltétel]:
#   (kód, ha a második feltétel True)
# else:
#   (kód, ha a második feltétel is FALSE)

# iterácis vezérlők, két fajta van:
# "előre meghatározott lépésszámú iterációs vezérlő":

# for [ciklus_változó] in [kollekció]:
#   [minden iterációban a ciklus_változó a kollekció soronkövetkező elemére hivatkozik]


# "feltételes iterációs vezérlő":
# while [feltétel]
#   (kód, ami akkor fog lefutni, ha a feltétel True)
#   (ha a Feltétel True, akkor a cikluson belüli kódrészlet megismétlődik)

# moduláris, kódszervező egységek

# függvények:
# def fg_neve (parameter_1:[p1_tipusa], parameter_2:[p2_tipusa], ...) -> [visszateresi_tipus]:
#   [fg_törzse]
#   ha a fg-nem van visszatérési típusa, akkor:
#   MINDEN lehetségeres ágon vissza kell térnie valamivel
#   na hohcs visszatérési típusa, akkor 'csak' elvégzi a dolgát, és kész

# pl. fg. definícióra:
def osszeadas (op_1:int, op_2:int) -> int:
    osszeg = op_1 + op_2
    return osszeg

# pl. fg. hívásra:
v:int = osszeadas(20, 30)

# pl. visszatérési típus nélküli fg. pl. (aka. 'eljárás'):
def koszon(nev:str) -> None:
    print(f'Szia {nev}!')
    print(f'Milyen szép név az, hogy {nev}! <3')

# pl. pn fg. hívásra:
koszon('Zsófi')
# azaz nem tudod (illetve hát nincs értelme) egyenlővé tenni valamivel

# osztályok
# egyelőre CSAK az adatstruktúra jellegét használtuk ki
# ebből a szempontból gyakorlatilag egy általunk definiált heterogén összetett típus

# tartalmaz egy 'anonim fg.', az ún. 'constructor'-t, ami az asztály (mint template) példányainak (mint konkrét értékkel rendelkező objektum) létrehozásáért felel. kötelező paramétere az __init__-nek a 'self', ami a későbbi konkrét objektumra magára való referencia
# class ClassNeve:
#   def __init__(self, p1:int, p2:str):
#       self.property_1:int = p1
#       self.property_2:str = p2

# pl class definícióra:
class Ember:
    def __init__(self, n:str, e:int):
        self.nev = n
        self.eletkor = e

# pl class példányosításra:
e:Ember = Ember('Lugosi Béla', 42)

# a 'class' konkrét páldányát 'object'-nek nevezzük, vagy úm. egy class instance-aként hivatkozunk rá.

# egy példány (osztály konstruktorában definiált) tulajdonságatit [példány_név].[tolajdonság_név] módon érjük el:
# pl:
e.eletkor = 20
print(e.eletkor)

# lényegében logikailag összetartozó adattagok csoportosítására használjuk [egyelőre]

# lehetséges osztályok példányait homogén módon listába rendezni

# pl. létre tudok hozni olyan listát, ami 'embereket' tartalmaz, azaz az általam deffiniált típus tagjait:

emberek:list[Ember] = [
    Ember('Para Zita', 25),
    Ember('Lapos Elemér', 30),
    Ember('Fá Zoltán', 32)
]

# -----------------------------------

# előredefiniált fg.k, amiket 'csak' felhasználunk:
# "osztályszintű fg.-k pl."
# range()
# print()
# input()
# len()

# [4, 6, 1, 3].sort() -> list
# "példányszintű" fg.-k pl:
# "VALAMI".lower() -> str
# "asd;~\n\n".strip() -> str
# "asd;asd;asd".split() -> list[str]

# nem 'minden' beépített "kódgyűjteményt" (modult) érünk el alapból, vannak, amiket külön kell impőortálnunk, pl:
# random
# math
# os

# és persze a saját magunk (vagy más, ún. 3rd party) által írt modulokat is...
# pl.:
# import my_module
# vagy
# from my_module import my_function

# -----------------------------------

# programozási tételek (nevezetes algoritmusok)
# sorozatszámítás
# szélsőérték meghatározás
# megszámlálás
# lineáris keresés
# kiválasztás
# eldöntés
# --------- (ezek még most nem kellenek)
# kiválogatás
# másolás
# metszetképzés/unióképzés
# ---------
# különböző rendezőalgoritmusok

# -----------------------------------

# amivel kiemelten foglalkoztunk az 'ún. filekezelés', pontosabban, hogy:
# "hogyan olvasunk be szabályosan strukturált tartalmú file-okat, objecteket tartalmazó homogén listákba, és ezeken hogyan alkalmazzuk a különböző nevezetes algoritmusokat a gyakorlati problémák megoldására"


# -> ellenőrzöm a file kódolását
# -> ellenőrzöm a szeparálókaraktert
# -> értelmezem az egy sorban lévő adattagokat
# -> logikai egység (a class) megtervezése
# -> file sorainak beolvasása
# -> file soraiból osztálypéldány létrehozása
# -> osztálypéldányok rögzítése honmogén listára
# -> honogén listán nevezetes algoritmusok alkalmazása