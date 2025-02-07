#Sozluk Dictionary Nedir?
#bir veri yapisidir anahtar-deger key-value ciftlerinden olusur
#{} ile  tanimlanir

#bir personelin kisisel bilgilerini iceren sozluk

person={
    "username":"Ahmet",
    "age":30,
    "city":"Adana"
}

print(person["username"])
print(person["age"])
print(person["city"])


#bos bir sozluk dictionary olustur

ogrenci={}

ogrenci["isim"] = "Mehmet"
ogrenci["not"]  = 85

print(ogrenci)