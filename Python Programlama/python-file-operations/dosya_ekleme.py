import os #dosya okuma işlemleri için kullanılan kütüphane import edilmesi gerekir
from ders10 import dosyayolu
dosyaEkle=open(dosyayolu(),"a")
with open(dosyayolu(),"a") as dosya:
     veri= input("Birşeyler yaz:")
     dosya.write(veri+"\n")
dosyaEkle.close()

