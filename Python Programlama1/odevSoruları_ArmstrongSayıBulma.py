# armstrong sayı

değer = int(input(" bir sayı giriniz : "))

geçiçiDeğer = değer
boş = 0


basamakSayısı = 0
while geçiçiDeğer != 0:

    kalan = geçiçiDeğer % 10
    geçiçiDeğer //= 10
    basamakSayısı += 1
print("", basamakSayısı)


while geçiçiDeğer != 0:

    kalan = geçiçiDeğer % 10
    geçiçiDeğer //= 10
    toplam = kalan ** 3
    boş = toplam+boş

if boş == değer:
    print(" {} sayısı bir armstrong sayıdır. ".format(değer))
else:
    print(" {} sayısı bir armstrong sayı değildir. ".format(değer))

print(" ")

# 1-1000 arasındaki tüm Armstrong sayıları yazdırınız.


for i in range(1, 1000):
    geçiçiDeğer = i
    result = 0
    while geçiçiDeğer != 0:
        kalan = geçiçiDeğer % 10
        toplam = kalan ** 3
        geçiçiDeğer //= 10
        result = toplam+result

    if result == i:
        print(" '{}' armstrong sayıdır ".format(i))


#  Bir sayının basamak sayılarının toplamını hesaplayan program yazınız.

number = int(input("bir sayı giriniz : "))

randomNumber = number
result = 0
while randomNumber != 0:
    kalan = randomNumber % 10
    randomNumber //= 10
    result = result+kalan

print("basamakların toplamı : {}".format(result))
