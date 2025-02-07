# sayının tersini hesaplama




sayı = int(input("sayı giriniz : "))

geciciSayı = sayı
tersSayı = 0

while geciciSayı != 0:
    kalan = geciciSayı % 10
    tersSayı = 0+kalan
    geciciSayı //= 10

print(" '{}' sayısının tersi '{}' sayısına eşittir.".format(sayı, tersSayı))
