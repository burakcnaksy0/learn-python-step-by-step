#Python'da Matplotlib Nedir ?
#veri gorsellestirme icin kullanilan bir moduldur

#ornek1 Basit bir Cizgi Grafigi Cizelim
import matplotlib.pyplot as plt 

#verileri olusturalim
x=[1,2,3,4,5]
y=[2,4,6,8,10]

#cizim yapalim
plt.plot(x,y)

#basliklari ve etiketleri olusturalim
plt.title("Basit Cizgi Grafigi")
plt.xlabel("X Ekseni")
plt.ylabel("Y Ekseni")
#Grafigi Goster
plt.show()