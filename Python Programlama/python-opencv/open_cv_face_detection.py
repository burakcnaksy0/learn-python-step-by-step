'''

OpenCV (Open Source Computer Vision Library),
acik kaynakli bir bilgisayar görüntüleme ve isleme kütüphanesidir.
Temelde gercek zamanli bilgisayar görüntü isleme,
nesne algilama, nesne takibi, yüz tanima, görüntü dönüsümleri,
kamera kalibrasyonu gibi bircok görevi yerine getirme amaciyla gelistirilmistir.

'''

import cv2

#Hazir olarak aldigimiz insan resmini cozumleyelim.
resim_yolu = 'human.jpg'# Tespit edilecek resmin yolunu belirtin
hedef_resim = cv2.imread(resim_yolu)

# Gri tonlamali hale getir
gray = cv2.cvtColor(hedef_resim, cv2.COLOR_BGR2GRAY)

# Yüz tespiti icin siniflandiriciyi yükle
yuz_siniflandirici = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')#bu xml dosyasini yüz tespiti icin hazir olarak github'dan temin ettim

# Yüzleri tespit et
hedef_yuzler = yuz_siniflandirici.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

#Tespit edilen yüzleri cerceve icine al
for (x, y, w, h) in hedef_yuzler:
    cv2.rectangle(hedef_resim, (x, y), (x + w, y + h), (0, 255, 0), 3)  # cerceve rengi ve kalinliği

# Sonucu göster
cv2.imshow('Hedefteki Resim Uzerinden Yuz Tespiti Yapma',hedef_resim)
cv2.waitKey(0)
cv2.destroyAllWindows()