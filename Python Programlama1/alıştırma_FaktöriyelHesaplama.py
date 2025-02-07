# faktöriyel hesaplama




# for döngüsüyle
faktorıyel = 1
sayı1 = int(input(" sayı giriniz  :"))
for i in range(1, sayı1+1):
    faktorıyel *= i

print("{}! = {}".format(sayı1, faktorıyel))


# while döngüsüyle
değer = 1
i = 1
while i <= sayı1:
    değer *= i
    i += 1

print("{}! = {}".format(sayı1, değer))



