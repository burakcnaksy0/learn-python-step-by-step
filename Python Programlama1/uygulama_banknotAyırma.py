# uygulama_banknot

girilenPara = int(input("lütfen para miktarını giriniz : "))

print('{} tane 200 banknotu bulunmaktadır'.format(girilenPara//200))
girilenPara %= 200
print('{} tane 100 banknotu bulunmaktadır'.format(girilenPara//100))
girilenPara %= 100
print('{} tane 50 banknotu bulunmaktadır'.format(girilenPara//50))
girilenPara %= 50
print('{} tane 20 banknotu bulunmaktadır'.format(girilenPara//20))
girilenPara %= 20
print('{} tane 10 banknotu bulunmaktadır'.format(girilenPara//10))
girilenPara %= 10
print('{} tane 5 banknotu bulunmaktadır'.format(girilenPara//5))
girilenPara %= 5


# uygulama_tersSayı

girilenSayı = int(input("lütfen 3 basamaklı bir sayı giriniz : "))
gecıcıSayı = girilenSayı
# 123
print(gecıcıSayı % 10, end='')
gecıcıSayı //= 10

print(gecıcıSayı % 10, end='')
gecıcıSayı //= 10

print(gecıcıSayı % 10, end='')
gecıcıSayı //= 10
