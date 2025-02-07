# ebob-ekok


# ebob = en büyük ortak bölen


sayı = int(input("sayı giriniz :"))

enBüyük = 1

for i in range(2, sayı):
    if sayı % i == 0:
        enBüyük = i

print("{} sayısısının EBOB'u {} sayısıdır.".format(sayı, enBüyük))


# ekok = en küçük ortak kat


sayı1 = int(input("sayı giriniz :"))
sayı2 = int(input("sayı giriniz :"))

maxNumber = 1

if sayı1 > sayı2:
    for i in range(2, sayı1):
        if sayı1 % i == 0 and sayı2 % i == 0:
            maxNumber = i
    print("{} ve {} sayısının EBOB'u {} sayısıdır.".format(sayı1, sayı2, maxNumber))


else:
    for i in range(2, sayı2):
        if sayı1 % i == 0 and sayı2 % i == 0:
            maxNumber = i
    print("{} ve {} sayısının EBOB'u {} sayısıdır.".format(sayı1, sayı2, maxNumber))


ekok = (sayı1*sayı2)//maxNumber

print("{} ve {} sayısının EKOK'u {} sayısıdır.".format(sayı1, sayı2, ekok))
