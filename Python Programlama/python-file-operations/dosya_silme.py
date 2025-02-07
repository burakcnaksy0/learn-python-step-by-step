import os #dosya okuma işlemleri için kullanılan kütüphane import edilmesi gerekir
import glob#dosyaları isimlerini kullanabilmek için glob import edilir
from ders10 import dosyayolu


if os.path.exists(dosyayolu()):
    os.remove(dosyayolu())
else:
    print("Böyle bir dosya bulunamadi !")    