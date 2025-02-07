# kaç basamalı oldugunu bulma


sayı = int(input("sayı giriniz : "))

basamakSayısı = 0
geciciSayı = sayı

while geciciSayı != 0:
    geciciSayı //= 10
    basamakSayısı += 1

print("{} sayısı {} basamaklıdır.".format(sayı, basamakSayısı))
