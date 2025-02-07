#Enumerate nedir ?
#dongulerler calisirken kullandigimiz oldukca faydali ve kullanisli bir methoddur
#dongu kurulurken hem elemanları hemde elemanların indekslerini aynı anda elde etmemizi saglar

#ornek1 Basit bir liste üzerinde enumerate

meyveler=["elma","armut","cilek"]

for indeks,meyve in enumerate(meyveler):
    print(f"{indeks}. {meyve}")

print("---------------------------")

#ornek2 Basit bir liste üzerinde enumerate   
 
renkler=["kirmizi","mavi","yesil","mor","sari"]

for indeks,renk in enumerate(renkler):
    print(f"{indeks}. {renk}")

print("---------------------------")

#ornek3 baslangic indeks'ini ayarlama

arabalar=["bmw","mercedes","audi","wolkswagen","kia","hyundai","peugeot"]

for indeks,araba in enumerate(arabalar,2):
    print(f"{indeks}. {araba}")        