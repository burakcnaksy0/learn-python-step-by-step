#Python'da İleri Seviye Fonksiyonlar (args, kwargs, lambda fonksiyonlari)

#1 *args ve **kwargs:
#Bu iki özel parametre,
#fonksiyonlara değişken sayıda argümanları geçmenizi sağlar.

#1- *args
def total(*args):
    sonuc=0
    for arg in args:
        sonuc +=arg
    return sonuc

print(total(1,2,3,4,5))


#2- **kwargs
def information(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}: {value}")

information(ad="Hakan",soyad="Yilmaz",yas=24)

#3-lambda fonksiyonlar
#Lambda fonksiyonları (isimsiz) işlevleri tanımlamak için kullanılır.
#Genellikle kısa ve tek seferlik kullanımlarda tercih edilir.

kare_al=lambda x: x ** 2
print(kare_al(5))

number_list=[1,3,5,6,8,10,9,4,2,7]

#lambda'da listeleme islemi yapacagiz
kupler=list(map(lambda x : x ** 3,number_list))
print("number list:",kupler)

#lambda'da liste filtreleme islemi yapacagiz burada cift olan sayilarin küpü alınıyor
number_filter=list(filter(lambda x : x % 2 == 0,number_list))
print("number filter:",number_filter)

#lambda'da liste siralama islemi yapacagiz burada sayilar buyukten kucuge listelenecek
number_sort=list(sorted(number_list,key=lambda x : -x))
print("number sort:",number_sort)

