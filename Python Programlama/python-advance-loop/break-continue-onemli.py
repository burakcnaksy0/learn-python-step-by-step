#break ile alakali dikkat edilmesi gerekenler nedir ?
#dongu dogru zamanda durdulurmali ve dongu bittikten sonra yapilacak islemler dogru planlanmalıdır
#aksi halde hesaplamalarda ciddi hata ve problemlerle karsilasabiliriz

#ornek 1 break ifadesinin for dongusunde dogru kullanimi
numbers=[1,2,3,4,5,6,7,8,9,10]
for number in numbers:
    if number == 5 :
        print("dongu sonlandiriliyor...")
        break # 5'e geldiginde dongu sona erdi
    print(f"sayi :{number}")
    
print("dongu kontrollu bir sekilde sonlandirildi.")

print("-----------------------------------------------")

#ornek2 continue ifadesinin for dongusunde dogru kullanimi
for number in numbers:
    if number % 2 == 0:
        continue
    print(f"Tek sayilar listele: {number}")   