#Python'da pandas nedir ?
#veri analizi icin kullanilan bir kutuphanedir

#ornek1 cesitli verilerin analizini yapan uygulama
import pandas as pd

#basit bir dataframe olusturalim
data={
    "Ad":["Ali","Ayse","Ahmet","Fatma"],
    "Yas":[23,45,35,28],
    "Sehir":["Istanbul","Ankara","Izmir","Antalya"]
}

df=pd.DataFrame(data)
#dataframe'i goruntuleyelim
print(df)

#ornek2 veriler dogrultusunda yas ortalamasini bulalim
print("\nYas Ortalamasi:",df["Yas"].mean())

#ornek3 veriler dogrultusunda hangi sehirde kac kisi var bulalim
print("\nSehirlerdeki Kisi Sayisi:\n",df["Sehir"].value_counts())

#ornek4 veriler dogrultusunda yasi 30'dan buyuk olan kisileri bulalim
print("\n Yasi 30'dan buyuk olanlar:\n",df[df["Yas"] >30])