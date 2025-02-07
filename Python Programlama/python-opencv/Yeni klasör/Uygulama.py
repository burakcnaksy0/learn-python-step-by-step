'''

OpenCV (Open Source Computer Vision Library),
acik kaynakli bir bilgisayar görüntüleme ve isleme kütüphanesidir.
Temelde gercek zamanli bilgisayar görüntü isleme,
nesne algilama, nesne takibi, yüz tanima, görüntü dönüsümleri,
kamera kalibrasyonu gibi bircok görevi yerine getirme amaciyla gelistirilmistir.

'''

import cv2

# Göz algılama sınıflandırıcısını yükle
goz_algilama = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# Görüntüyü yükle
hedef_resim = cv2.imread('hedef_resim.jpg')
renk = cv2.cvtColor(hedef_resim, cv2.COLOR_BGR2GRAY)

# Gözleri algıla
goz = goz_algilama.detectMultiScale(renk, scaleFactor=1.3, minNeighbors=5)

# Algılanan gözleri çerçevele
for (x, y, w, h) in goz:
    cv2.rectangle(hedef_resim, (x, y), (x+w, y+h), (255, 0, 0), 2)

# Sonuç görüntüsünü göster
cv2.imshow('Goz Algilama ve Tespit Edilmesi',hedef_resim)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Yukarıdaki uygulamada, önceden eğitilmiş göz algılama sınıflandırıcısı kullanarak görüntüdeki gözleri tespit ettik.
#Örnek uygulamamizi kendi gereksinimlerinize göre uyarlayabilirsiniz.
#Gözlerin çerçevelendiği renk, kalınlık ve diğer özellikleri de degistirmenizde mumkundur

#Görüntü yolunu hedef_resim.jpg olarak  OpenCV sürümünüze gore kaydetmemiz gerekiyor.