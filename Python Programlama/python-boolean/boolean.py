#ornek1
a=10
b=5
hangisi_buyuktur= a < b
print(hangisi_buyuktur)

#ornek2
meyveler=["elma","muz","cilek","portakal"]
hangi_meyve=meyveler[0] == "elma"
print(hangi_meyve)

#ornek3
durumlar=[True,False,True,False,True]
print(durumlar)

#ornek4
sayilar=[1,2,3,4,5,6]
cift_mi=[sayi % 2 == 0 for sayi in sayilar]
print(cift_mi)

#ornek5
degerler=(5>3,10 == 10,7 < 4, "Python" == "python", len("hello") == 5)
print(degerler)