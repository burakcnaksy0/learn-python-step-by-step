#python'da random modülü nedir?
#python'da rastgele sayilar ve degerler uretmek icin kullanılan modüle random denir.

#ornek1 1 ile 10 arasinda 5 adet rastgele sayi üretelim
import random

for i in range(5):
    rastgele_sayi=random.randint(1,10)
    print(f"Rastgele sayi {i+1}: {rastgele_sayi}")

#ornek2 rastgele sayi tahmini uygulamasi
dogru_sayi=random.randint(1,5)
tahmin=0

while tahmin != dogru_sayi:
    tahmin=int(input("1 ile 5 arasinda bir sayi tahmin ediniz:"))
    if tahmin == dogru_sayi:
        print("Tebrikler dogru sayiyi tahmin ettiniz !")
    else:
        print("yanlis tahminde bulundunuz !")        