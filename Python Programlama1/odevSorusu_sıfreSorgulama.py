#  sıfre sorgulama

password = input(" lütfen şifreyi giriniz : ")
sayıSorgusu = False
kucukHarfSorgusu = False
buyukHarfSorgusu = False
karakterSayısı = 0

for ch in password:
    if buyukHarfSorgusu == False and ch >= 'A' and ch <= 'Z':
        buyukHarfSorgusu = True
    elif kucukHarfSorgusu == False and ch >= 'a' and ch <= 'z':
        kucukHarfSorgusu = True
    elif sayıSorgusu == False and ch >= '1' and ch <= '9':
        sayıSorgusu = True
    karakterSayısı += 1

if buyukHarfSorgusu == False:
    print(" lütfen büyük harf kullanınız !!")
elif kucukHarfSorgusu == False:
    print(" lütfen küçük harf kullanınız !!")
elif sayıSorgusu == False:
    print(" lütfen bir rakam kullanınız !!")
elif karakterSayısı < 8:
    print(" şifre minimum 8 karakterli olmalıdır.")
elif karakterSayısı > 16:
    print(" şifre maksimum 16 karakter olmalıdır.")
else:
    print(" şifreniz uygundur")
