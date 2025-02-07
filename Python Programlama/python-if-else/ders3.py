#Python'da Kosullu ifadeler ve karar yapilari

#programlarınızın belirli şartlara göre
#farklı davranışlar sergilemesini sağlar.

#not 50 den dusukse ogrenci dersten kaldi

sinavPuani=67

if sinavPuani<50:
    print("ogrenci dersten kaldi")

else:
    print("ogrenci dersten gecti")

#hava sicakli -10 10 derece arasi ise hava soguk
#10 20 derece arasi ise hava normal
#20 50 derece arasi ise hava sicak

havaSicakligi=15

if havaSicakligi>-10 and havaSicakligi<10:
    print("Hava soguk")

elif havaSicakligi>=10 and havaSicakligi<=20:
    print("Hava normal")

elif havaSicakligi>20 and havaSicakligi<=50:
    print("Hava sicak")

else:
    print("Hava sicakligi olculemedi !")            