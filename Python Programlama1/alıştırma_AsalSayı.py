# asal sayı sorgualama

sayı = int(input("sayı giriniz :"))

isPrime = False

for i in range(2, sayı):
    if sayı % i == 0:
        isPrime = True
        break

if isPrime:
    print("{} sayısı asal sayı değildir.".format(sayı))
else:
    print("{} sayısı asal sayıdır.".format(sayı))
