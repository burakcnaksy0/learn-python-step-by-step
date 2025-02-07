# function

'''

syntax yapısı;

def fonksName(parameter):
    yapılacakIslemler

'''


def greetings():
    print("hi girls")


greetings()


def sa(name):
    print("sa {}".format(name))


sa("burak")


def elemanYazdır(*sayılar):     # parametre sayısı belli değilse kullanılır.
    for sayı in sayılar:
        print(sayı, end=" ")
    print(end="\n")


elemanYazdır(13, 43, 12, 3, 65, 123, 64, 132, 6, 1)


def topla(sayı1, sayı2):
    return sayı1+sayı2


result = topla(2, 5)
print(result)


def listeBuyukKucuk(liste):
    liste.sort()
    enBuyuk = liste[-1]
    enKucuk = liste[0]
    return enBuyuk, enKucuk


list = listeBuyukKucuk([1, 32, 54, 21, 654, 12, 213, 67, 23, 7, 3, 0])
print(list)


def faktorıyelHesapla(sayı):
    if sayı == 1:
        return 1
    return sayı*faktorıyelHesapla(sayı-1)


ss = faktorıyelHesapla(7)
print(ss)



def sayıDeğişstir(x):
    print(x)
    x=5#local değişken
y=10#global değişken



