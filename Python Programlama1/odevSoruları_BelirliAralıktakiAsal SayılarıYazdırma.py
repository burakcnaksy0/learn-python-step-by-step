# Belirli Aralıktaki Asal Sayıları Yazdırma

değer = int(input(" bir sayı giriniz : "))
değer1 = int(input(" bir sayı giriniz : "))


for i in range(değer, değer1+1):

    isPrime = True
    for j in range(2, i):
        if i % j == 0:
            isPrime = False
            break
    if isPrime:
        print(i, end=(" "))
