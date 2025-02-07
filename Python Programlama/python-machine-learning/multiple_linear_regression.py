'''
Çoklu doğrusal regresyon, makine öğrenmesinde kullanılan istatistiksel bir yöntemdir.
Bu yöntem, birden fazla bağımsız değişkenin bir bağımlı değişken üzerindeki ilişkisini modellemek için kullanılır.

Çoklu doğrusal regresyon denklemi şu şekilde ifade edilir = y = b0 + b1x1 + b2x2 + ... + bn*xn

y: Bağımlı değişken (tahmin edilmeye çalışılan değerler)
x1, x2, ..., xn: Bağımsız değişkenler (girdi özellikleri)
b0: Kesme terimi (intercept), denklemin y eksenini kestiği noktayı ifade eder
b1, b2, ..., bn: Eğim (slope) terimleri, her bir bağımsız değişkenin bağımlı değişken üzerindeki etkisini ifade eder

özetle Çoklu doğrusal regresyon modeli buradaki verilerin arasindaki ilişkiyi temsil etmek için bu terimleri bulma üzerine yogunlasir,

Eğitim sürecinde uygun eğim(slope) ve kesme terimleri(intercept) hesaplanir.
Bu parametreler belirlendikten sonra, model yeni verilere tahminlerde bulunabilir.

Python'da, scikit-learn gibi kütüphaneleri kullanarak çoklu doğrusal regresyon modelleri oluşturabilir, eğitebilir ve tahminler yapabilirsiniz. Örnek bir kullanımı aşağıda görebilirsiniz:
'''

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


# Örnek1  girilen ev bilgilerine göre ev fiyat tahmininde bulunacagimiz coklu dogrusal regresyon modeli oluşturma ve ev fiyat tahmininde bulunma
np.random.seed(0)
ev_buyuklugu = np.random.randint(100, 300, 100)
oda_sayisi = np.random.randint(2, 6, 100)
ev_konumu = np.random.randint(1, 5, 100)
bina_yasi = np.random.randint(5, 30, 100)
ev_fiyati = 200000 + (ev_buyuklugu * 100) + (oda_sayisi * 5000) + (ev_konumu * 20000) - (bina_yasi * 1500) + np.random.randint(-50000, 50000, 100)


ev_bilgileri = pd.DataFrame({
    'ev_buyuklugu': ev_buyuklugu,
    'oda_sayisi': oda_sayisi,
    'ev_konumu': ev_konumu,
    'bina_yasi': bina_yasi,
    'ev_fiyati': ev_fiyati
})

# Bağımsız değişkenler (x) ve bağımlı değişken (y)
x = ev_bilgileri[['ev_buyuklugu', 'oda_sayisi', 'ev_konumu', 'bina_yasi']]
y = ev_bilgileri['ev_fiyati']

# veriyi eğitim ve test setlerine bölelim
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2, random_state=42)

# Modeli oluşturup eğitelim
model = LinearRegression()
model.fit(x_train,y_train)

# Test seti üzerinde tahmin yapalım
tahminler = model.predict(x_test)

# Modelin performansını değerlendirelim
mse = mean_squared_error(y_test, tahminler)
print(f"Ortalama Kare Hata (MSE): {mse}")