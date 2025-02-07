"""a = input("bir değer giriniz :")       # burda girilen tam sayı değeri string bir değişken olarak alınır.
print(a)                               # istenilen işlemleri yapabilmemiz için integer ifadeye dönüştürmek gerekir.
a = int(a)+1
print(a)


# print fonksiyonunda kulanılan bazı özel karakterler

print("burakcan\naksoy\nberat\naksoy")     # \n bi alt satıra geçer

print("burakcan\taksoy")    # bir tab boşluk koyar

print("burakcan \baksoy")    # bir boşluk siler


# end kavramı

print("burakcan aksoy", end="\n:)")

# sep kavramı
print("burak", "aksoy", "merhaba", "dünya", sep=",")
print(*"burakcan aksoy", sep=",")
"""


b =int(input("entry a value"))
print(b*b)

