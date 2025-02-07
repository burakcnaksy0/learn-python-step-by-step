#ogrencinin notunu sisteme girelim
ogrenci_notu=int(input("Ogrencinin Notunu Sisteme Giriniz:"))

if ogrenci_notu>=90:    #90-100 ARASI
    harf_notu= "AA"
elif ogrenci_notu >=85: #85-89 ARASI
    harf_notu= "BA"
elif ogrenci_notu >=75: #75-84 ARASI
    harf_notu= "BB"        
elif ogrenci_notu >=60: #60-74 ARASI
    harf_notu= "CB"
elif ogrenci_notu >=50: #50-59 ARASI
    harf_notu= "CC"
elif ogrenci_notu >=45: #45-49 ARASI
    harf_notu= "DC"
else:
    harf_notu= "FF"

print(f"Ogrencinin Harf Notu: {harf_notu}")         
     
       