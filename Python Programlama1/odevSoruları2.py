#  Basamak Sayısı Hesaplama

import random

rastgeleSayı = random.randint(1, 99999)

if rastgeleSayı // 10000 > 0:
    print("{} 5 basamaklı sayıdır.".format(rastgeleSayı))

elif rastgeleSayı // 1000 > 0:
    print("{} 4 basamaklı sayıdır.".format(rastgeleSayı))

elif rastgeleSayı // 100 > 0:
    print("{} 3 basamaklı sayıdır.".format(rastgeleSayı))

elif rastgeleSayı // 10 > 0:
    print("{} 2 basamaklı sayıdır.".format(rastgeleSayı))

else:
    print("{} tek basamakli sayıdır.".format(rastgeleSayı))


#  Alışveriş-Fiyat Hesaplama

alısverisTutarı = random.randint(1, 10000)
print("alışveriş tutarınız {} ₺ ".format(alısverisTutarı))

taksitKontrol = input("taksit istermisiniz ?(E-H) : ")
if taksitKontrol == 'E' or taksitKontrol == 'e':
    print("taksit uygulama ekranı")
    taksitSayı = input("kaç taksit istersiniz ? (3-6-9)  :")
    if taksitSayı == '3':
        print("3 taksit uygulanıyor.")
        alısverisTutarı += alısverisTutarı*0.03
        print("taksit sonrası tutar {} ₺".format(alısverisTutarı))
    elif taksitSayı == '6':
        print("6 taksit uygulanıyor.")
        alısverisTutarı += alısverisTutarı*0.06
        print("taksit sonrası tutar {} ₺".format(alısverisTutarı))
    elif taksitSayı == '9':
        print("9 taksit uygulanıyor.")
        alısverisTutarı += alısverisTutarı*0.09
        print("taksit sonrası tutar {} ₺".format(alısverisTutarı))

else:
    print("taksit uygulanmıyor..")

alısverısKartKontrol = input("alışveriş kartınız var mı ?(E-H) :  ")
if alısverısKartKontrol == 'E' or alısverısKartKontrol == 'e':
    print("indirim uygulama")
    alısverisTutarı -= alısverisTutarı*0.1
    print("indirim sonrası tutar {} ₺".format(alısverisTutarı))

else:
    print("herhangi bir indirim uygulamıyor..")

print("son tutar : {}".format(alısverisTutarı))
