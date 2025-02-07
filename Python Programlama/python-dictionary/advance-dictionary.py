#ornek1
kareler={x:x**2 for x in range(1,6)}
print(kareler)

#ornek2
sozluk1={"ad":"Ayse","yas":25}
sozluk2={"sehir":"Ankara","meslek":"muhendis"}
birlestirilmis_sozluk=sozluk1 | sozluk2
print(birlestirilmis_sozluk)

#ornek3
kisi={"ad":"Zeynep","yas":32}
sehir=kisi.get("sehir","Bilinmiyor")
print(sehir)

#ornek4
ogrenciler={"Ali":85,"Ayse":80,"Mehmet":90}
for isim,notu in ogrenciler.items():
    print(f"{isim} adli ogrencinin notu:{notu}")
    
#ornek5
renkler={"kirmizi":"#FF000","yesil":"00FF00","mavi":"0000FF"}

#anahtar listesi key
anahtarlar=list(renkler.keys())
print(anahtarlar)    

#degerler listesi value
degerler=list(renkler.values())
print(degerler)