#python'da hata yakalama ve istisna yonetimi
#try ve except sayesinde programınız çalışırken
#oluşabilecek hataları yakalayabilir istisnaya özel işlemler
#gerçekleştirebilirsiniz.

#ornek 1

try:
    sayi=int(input("Bir sayi giriniz:"))
    sonuc=10 / sayi
    print("Sonuc :",sonuc)
except ZeroDivisionError:
    print("Hata:","Bir sayi 0 a bolunemez !")
except ValueError:
    print("Hata:","Geçerli bir sayi girmediniz !")
except Exception as e :
    print("Beklenmeyen bir hata olustu",e)
finally:
    print("Islem tamamlandi !")

#ornek2

while True:
        try:
            vize = float(input("Vize notunu girin: "))
            
            final = float(input("Final notunu girin: "))
        
            if 0 <= vize <= 100 and 0 <= final <= 100:
                toplam_not = vize * 0.4 + final * 0.6
                if toplam_not >= 90:
                    print("AA")
                elif toplam_not >= 85:
                    print("BA")
                elif toplam_not >= 80:
                    print("BB")
                elif toplam_not >= 75:
                    print("CB")
                elif toplam_not >= 70:
                    print("CC")
                elif toplam_not >= 65:
                    print("CC")
                elif toplam_not >= 60:
                    print("DD")
                else:
                    print("FF (Kaldiniz)") 
            else:
                print("Hatali giriş! Notlar 0 ile 100 arasinda olmali.")
        except ValueError:
            print("Hatali giriş! Lütfen sayisal değerler girin.")
        
        finally:
            print("Sinav sonucu:",toplam_not)                        