'''
Makine öğrenmesinde, basit doğrusal regresyon, istatistiksel bir yöntemdir.
bağimli ve bağimsiz değişkenler arasindaki ilişkiyi modellemek için kullanilir.
tek bir bağimsiz değişkenin bağimli değişken üzerindeki etkisini anlamak için kullanilir.

Basit doğrusal regresyon, bu bağimli-değişken ilişkisini doğrusal bir denklemle ifade eder y=mx+b

y, bağimli değişken (tahmin edilmeye çalişilan değerler)
x, bağimsiz değişken (girdi özellikleri)
m, eğim (slope), bağimsiz değişkenin bağimli değişken üzerindeki etkisini ifade eder
b, kesme terimi (intercept), doğrunun y eksenini kestiği noktayi ifade eder

Python'da, sklearn gibi kütüphaneler kullanarak basit doğrusal regresyon modelleri oluşturabilir, eğitebilir ve tahminler yapabilirsiniz.

'''
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from PIL import Image
#basit bir doğrusal regresyon modeli ile Ornek veriyi analizi
x = np.array([1,3,6,8,11]).reshape(-1, 1)
y = np.array([2.25,3.7,4.6,5.8,8.3])

# Doğrusal regresyon modelini oluşturma
model = LinearRegression()
model.fit(x,y)

# Eğim (slope) ve kesme terimi (intercept) elde etme
egim = model.coef_[0]
kesme_terimi = model.intercept_

#Tahminler yapma
tahminler = model.predict(y)

# Veriyi ve doğruyu grafiğe çizdirme
plt.scatter(x, y, label='Gerçek Veri')
plt.plot(x, tahminler, color='red', label='Doğru Regresyon')
plt.xlabel('Bagimsiz Değişken')
plt.ylabel('Bagimli Değişken')
plt.title('Basit Doğrusal Regresyon')
plt.legend()
plt.show()

#Tahmin yapma
yeni_x_degeri = np.array([6]).reshape(-1, 1)
yeni_tahminler = model.predict(yeni_x_degeri)
print(f'6 birimlik girdi için tahmin: {yeni_tahminler[0]:.2f}')



#ornek2 makine ogrenmesi ile Örnek veri oluşturma
np.random.seed(0)
Ozellikler = np.random.rand(100, 2)  # 100 örnek, 2 özellik
Hedef = 3 * Ozellikler[:, 0] + 5 * Ozellikler[:, 1] + 2 + np.random.randn(100)  # Gerçek fonksiyon: 3x1 + 5x2 + 2 + hata

# Veriyi eğitim ve test kümelerine ayirma
Ozellikler_egitim, Ozellikler_test, Hedef_egitim, Hedef_test = train_test_split(Ozellikler, Hedef, test_size=0.2, random_state=42)

# Doğrusal regresyon modelini oluşturma ve eğitme
model = LinearRegression()
model.fit(Ozellikler_egitim, Hedef_egitim)

# Eğitim kümesi üzerinde tahminler yapma
Hedef_egitim_tahmin = model.predict(Ozellikler_egitim)

# Test kümesi üzerinde tahminler yapma
Hedef_test_tahmin = model.predict(Ozellikler_test)

# Hata hesaplamalari
egitim_mse = mean_squared_error(Hedef_egitim, Hedef_egitim_tahmin)
test_mse = mean_squared_error(Hedef_test, Hedef_test_tahmin)

#Sonuclari yazdirma
print("Eğitim kümesi Ortalama Kare Hatasi:", egitim_mse)
print("Test kümesi Ortalama Kare Hatasi:", test_mse)


#Test kümesi verilerini ve tahminleri grafiğe çizdirme
plt.scatter(Hedef_test, Hedef_test_tahmin)
plt.xlabel("Gerçek Değerler")
plt.ylabel("Tahmin Edilen Değerler")
plt.title("Gerçek Değerler vs. Tahmin Edilen Değerler")
plt.show()