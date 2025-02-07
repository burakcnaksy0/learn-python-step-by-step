#break nedir ?
#bir donguyu tamamen sonlandırmak icin break kullanılır.

#ornek1 break ile donguden cikis

for i in range(1,11):
    print(i)
    if i == 5:
        print("Dongu 5'te sonlandirildi !")
        break

#continue nedir ?
#bir dongude belirtilen index'in atlanmasina geçilmesine continue denir.

print("--------------------------------------")

#ornek2 continue ile iterasyonu atlama

for i in range(1,6):
    if i == 3:
        print("x degeri atlandi gecildi !")
        continue
    print(i)   