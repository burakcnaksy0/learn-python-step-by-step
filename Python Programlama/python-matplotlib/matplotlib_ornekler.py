import matplotlib.pyplot as pyplt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

#ornek1 sayilarin karesine gore geometrik artıs saglayan cizgi grafigi 
x_ekseni=[1,2,3,4,5,6,7]
y_ekseni=[1,4,9,16,25,36,49]

pyplt.plot(x_ekseni,y_ekseni,marker='o')# cizgi grafigini tanimladik

pyplt.xlabel('X Koordinati')#x eksenine ait label tanimlandi
pyplt.ylabel('Y Koordinati')#y eksenine ait label tanimlandi
pyplt.title('Cizgi Grafigi')#grafigin basligini tanimladik

pyplt.show()

# #ornek2 rastgele verilen sayilarin dagilimini yapan grafik
random_data=np.random.normal(size=1000)#rastgele veriler olusturduk  boyutunu 1000 olarak ayarladik

pyplt.hist(random_data,bins=18,density=True,alpha=0.6,color='orange') #dagilim grafigini tanimladik
pyplt.title('Normal Dagilim Grafigi')

pyplt.xlabel('Veriler')
pyplt.ylabel('Yogunluk')
pyplt.grid(True)#grafigin arkasinda izgara olusturduk

pyplt.show()


# #ornek3 futbolcularin bir sezonda attiklari gole gore sutun grafigini olusturma
futbolcu=['Arda','Emre','Hakan','Cenk','Oguzhan','Yusuf']
gol_sayisi=[15,23,21,25,30,20]

pyplt.bar(futbolcu,gol_sayisi)#sutun grafigi cizdirildi
pyplt.xlabel('Futbolcu listesi')
pyplt.ylabel('Gol sayisi')
pyplt.title('En fazla Gol Atan Oyuncular')

pyplt.show()


# #ornek4 aylik yaptigimiz harcamalarimiza gore pasta grafigi olusturma

harcamalar=['ulasim','yemek','kira','market','elektronik esya']
harcama_miktarlari=[1200,4500,5000,3000,8000]

pyplt.figure(figsize=(10,10))#grafigin boyutunu 10 a 10 a olacak sekilde olusturduk
pyplt.pie(harcama_miktarlari,labels=harcamalar,autopct='%1.0f%%',startangle=120)

pyplt.axis('equal')#dairenin tam olarak ayarlamasini yapar
pyplt.title('Aylik harcamalarin Pasta Grafigi')

pyplt.show()


#ornek5 3d ile yüzelsel bir grafik olusturma
x_ekseni = np.linspace(-8, 8, 64)
y_ekseni = np.linspace(-8, 8, 64)

x_ekseni, y_ekseni = np.meshgrid(x_ekseni, y_ekseni)

z_ekseni = np.sin(np.sqrt(x_ekseni**2 + y_ekseni**2))  # Hatalı ifade düzeltildi

fig = pyplt.figure()  # 3B bir figura oluşturduk

axes = fig.add_subplot(111, projection='3d')  # subplot düzeltildi

surface = axes.plot_surface(x_ekseni, y_ekseni, z_ekseni, cmap='viridis')  # Z ekseni düzeltildi

fig.colorbar(surface)

#Eksen etiketlerini ayarla
axes.set_xlabel('X Ekseni')
axes.set_ylabel('Y Ekseni')
axes.set_zlabel('Z Ekseni')
axes.set_title('3B Yüzey Grafiği Örneği')

# # Görselleştirmeyi göster
pyplt.show()



#ornek6 gomulu metin ve anotasyonlar
a = np.linspace(0, 10, 100)
b = np.sin(a)

pyplt.plot(a, b)
pyplt.xlabel('a değerleri')
pyplt.ylabel('b değerleri')
pyplt.title('gömülü metin ve annotasyonlar')
pyplt.text(2, 0.5, 'önemli nokta', fontsize=12, color='red')
pyplt.annotate('tepe noktasi', xy=(np.pi/2, 1), xytext=(3, 1.5),
               arrowprops=dict(facecolor='black', shrink=0.05))
pyplt.show()

#ornek7 polar alt eksenler
theta = np.linspace(0, 2*np.pi, 100)
r = np.sin(6*theta)

figure = pyplt.figure()
axes = figure.add_subplot(111, projection='polar')
axes.plot(theta, r, label='Sinüs Fonksiyonu')
axes.set_title('Polar Alt Eksenler')
axes.legend()
pyplt.show()


#ornek8 3d Cubuk Grafigi
a = np.arange(1,6)
b = np.array([12, 23, 17, 25, 18])
c = np.array([1, 2, 3, 4, 5])

fig = pyplt.figure()
axes = fig.add_subplot(111, projection='3d')

axes.bar(a, b, c, zdir='y', color=['red', 'green', 'blue', 'purple', 'orange'])
axes.set_xlabel('A Değerleri')
axes.set_ylabel('B Değerleri')
axes.set_zlabel('C Değerleri')
axes.set_title('3D Çubuk Grafikleri')
pyplt.show()


#ornek9 Renk Gradyanlari

a = np.linspace(0, 5, 100)
b = a**2

figure,axes =pyplt.subplots()
axes.fill_between(a, b, color='green', alpha=0.3)
axes.fill_between(a, b*1.2, b*1.5, color='red', alpha=0.3)
axes.set_xlabel('X Değerleri')
axes.set_ylabel('Y Değerleri')
axes.set_title('Renk Gradyanları')
pyplt.show()


#ornek10 Renk Haritalari Colormapsler
renk_verileri = np.random.rand(18,18)

pyplt.imshow(renk_verileri, cmap='viridis', interpolation='nearest')
pyplt.colorbar()
pyplt.title('Renk Haritaları')
pyplt.show()


#ornek11 Veri Gorsellestirme ile Dogrusal Regresyon Ornegi
np.random.seed(0)
a = np.random.rand(50)
b = 2 * a + 1 + 0.1 * np.random.randn(50)

pyplt.scatter(a, b, label='Gerçek Veri')
pyplt.plot(a, 2 * a + 1, color='red', label='Doğrunun Regresyonu')
pyplt.xlabel('A Değerleri')
pyplt.ylabel('B Değerleri')
pyplt.title('Doğrusal Regresyon')
pyplt.legend()
pyplt.show()

#ornek12 İleri Veri Gorsellestirme Isı Haritasi(Heatmap)
veriler = np.random.rand(17, 17)

pyplt.imshow(veriler, cmap='coolwarm', interpolation='nearest')
pyplt.colorbar()
pyplt.title('Isı Haritası (Heatmap)')
pyplt.show()

#ornek13 Coklu Veri Setleri ile Alt grafikler olusturma 
x = np.linspace(0, 5, 100)
y1 = x
y2 = x**2
y3 = x**3

figure, axes = pyplt.subplots(nrows=1, ncols=3, figsize=(15, 5))
axes[0].plot(x, y1)
axes[0].set_title('Lineer Fonksiyon')
axes[1].plot(x, y2)
axes[1].set_title('Kare Fonksiyon')
axes[2].plot(x, y3)
axes[2].set_title('Küp Fonksiyon')

for ax in axes:
    ax.set_xlabel('X Değerleri')
    ax.set_ylabel('Y Değerleri')

pyplt.tight_layout()
pyplt.show()


#ornek14 Dagilim Gosterimi ile Cift Eksenli Histogram Olusturma ornegi
veri1 = np.random.randn(1000)
veri2 = np.random.randn(1000) + 2

figure, axes1 = pyplt.subplots()

axes1.hist(veri1, bins=30, alpha=0.5, label='Veri 1')
axes1.set_xlabel('Değer Aralığı')
axes1.set_ylabel('Frekans', color='tab:blue')
axes1.tick_params(axis='y', labelcolor='tab:blue')

axes2 = axes1.twinx()
axes2.hist(veri2, bins=30, alpha=0.5, color='orange', label='Veri 2')
axes2.set_ylabel('Frekans', color='tab:orange')
axes2.tick_params(axis='y', labelcolor='tab:orange')

fig.suptitle('Çift Eksenli Histogram')
fig.legend(loc='upper right')
pyplt.show()


#ornek15 3d ile Yuzey Grafigi Olusturma
x = np.linspace(-5, 5, 50)
y = np.linspace(-5, 5, 50)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))

fig = pyplt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(X, Y, Z, cmap='coolwarm')
ax.set_xlabel('X Ekseni')
ax.set_ylabel('Y Ekseni')
ax.set_zlabel('Z Ekseni')
ax.set_title('3D Yüzey Grafiği')
pyplt.show()