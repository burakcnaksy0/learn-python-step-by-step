# Delta Değeri Hesaplama

a = int(input("bir a değeri giriniz  :"))
b = int(input("bir b değeri giriniz  :"))
c = int(input("bir c değeri giriniz  :"))

deltaFormula = b**2 - 4*a*c
print("delta = {}".format(deltaFormula))
print("deltanın 0 dan büyük-küçük durumu : ", deltaFormula > 0)


# Vize-Final Notu ile Ortalama Hesaplama

vizeNot = int(input("vize notunuzu giriniz : "))
finalNot = int(input("final notunuzu giriniz : "))

ortalama = vizeNot*0.4 + finalNot*0.6
print("ortalama = {}".format(ortalama), "=>>", ortalama > 60)


# Daire Alan-Çevre Hesaplama

r = int(input("yarıçap değeri giriniz : "))

pi = 3.14
daireAlan = pi*r**2
daireCevre = 2*pi*r
print("daire alanı :{}".format(daireAlan))
print("daire çevresi :{}".format(daireCevre))
