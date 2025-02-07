#Python'da fonksiyonlar ve Moduller

#fonksiyonlar ve modüller,
#kodunuzu daha düzenli, yönetilebilir,
#tekrar kullanılabilir hale getirmenize yardımcı olan
#temel kavramlardır.

print("--------------Fonksiyonlar Konusu Ornekleri--------------")
#1-)parametre almayan fonksiyon
def mesaj():
    print("Python Dersleri basladi !")

mesaj()

#2-)parametre alan fonksiyon
def uslu_sayi(taban,kuvvet):
    sonuc=taban**kuvvet
    return sonuc

sonuc2=uslu_sayi(taban=7,kuvvet=2)
print(sonuc2)

#3-)fonksiyon kullanarak sayi tahmin oyunu
import random
import time
def sayiyiTahmiEt():
    tahminEdilecekSayi=random.randrange(1,10000)
    tahminEtmeHakki=18
    
    print("Sayi Tahmin Etme Oyunu Basliyor...")
    time.sleep(2)
    while tahminEtmeHakki>0:
        print("Tahmin Etme Hakkiniz:",tahminEtmeHakki)
        tahmininiz=int(input("Sayiyi Tahmin Edin:"))
        if tahmininiz<tahminEdilecekSayi:
            print("Tahminini Yukselt")
        elif tahmininiz>tahminEdilecekSayi:
            print("Tahminini Dusur")
        else:
            print(f"Tebrikler {tahminEdilecekSayi} dogru tahmin ettiniz !")
            break 
        
        tahminEtmeHakki -=1
        if tahminEtmeHakki ==0:
            print(f"Tahmin Hakkiniz bitti Sayi:{tahminEdilecekSayi}")
           
sayiyiTahmiEt()

print("--------------Moduller Konusu Ornekleri--------------")

#moduller matematik modulu olusturduk ve dahil ettik 
import matematik

matematik.cift_sayilari_al(1,33)

matematik.kare_al(8)

matematik.mod_al(35,3)

matematik.sansli_sayi(1,5000)