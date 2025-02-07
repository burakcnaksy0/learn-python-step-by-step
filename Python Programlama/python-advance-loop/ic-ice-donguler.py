#veri isleme nedir ?
#birden fazla boyutta veri setlerini islemek icin donguleri ic-ice kullanırız
#bu yontem genellikle cokboyutlu dizilerde
#(listeler,matrisler veya tablolar) uzerinde islem yaparken kullanılır.

#ornek1 2 boyutlu bir listeyi isleme
notlar=[
    [90,80,85],
    [78,88,84],
    [92,70,75],
    [55,93,100]
]

#her ogrencinin ortalama notunu hesaplayalim
for ogrenci in range(len(notlar)):
    toplam=0
    for notu in notlar[ogrenci]:
        toplam +=notu
    ortalama=toplam /len(notlar[ogrenci])
    print(f"{ogrenci + 1}. Ogrencinin ortalama notu: {ortalama}")    

print("-------------------------------------------")

#ornek2 3x3 matrisin transpozunu hesaplayalim

matris=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
#matrisin transpozunu alalim
transpoz = [[0,0,0] for _ in range(3)]

for i in range(len(matris)):
    for j in range(len(matris[i])):
        transpoz[j][i] = matris[i][j]

#transpoz matrisini yazdiralim
for satir in transpoz:
    print(satir)        
        