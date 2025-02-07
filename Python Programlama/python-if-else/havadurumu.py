#sistemden sicaklik degerini alalim
sicaklik=float(input("Sicaklik degeri giriniz (Celsius):"))

#Hava Durumunu Sicakliga Gore Belirleme
if sicaklik < 0:
    hava_durumu= "Soguk"
elif 0 <= sicaklik < 15:
    hava_durumu= "Serin"
elif 15 <= sicaklik < 25:
    hava_durumu= "Normal"
elif 25 <= sicaklik < 35:
    hava_durumu= "Sicak"
else:
    hava_durumu= "Asiri Sicak"

#sonucu yazdir
print(f"Hava durumu: {hava_durumu}")                    