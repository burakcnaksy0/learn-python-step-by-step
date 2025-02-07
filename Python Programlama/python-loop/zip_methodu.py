#python'da zip methodu nedir ?
#bir method'du ve birden fazla iterable üzerinde aynı anda dongu olusturur.

#ornek1 iki listeyi birlestirme
names=["ali","veli","ayse"]
ages=[25,30,22]

#iki listeyi zip ile birlikte birlestirip her bir cifti yazalim
for name,age in zip(names,ages):
    print(f"{name} {age} yasinda")

#ornek2 üç farklı listeyi birleştirme
ogrenci=["mahmut","emir","berk"]
notlar=[85,95,78]
devamlilik=[95,80,75]

#üç listeyi zip ile birlikte birlestirip her bir cifti yazalim
for student,grade,attend in zip(ogrenci,notlar,devamlilik):
    print(f"{student}, Notu:{grade}, Devam:%{attend}")
    