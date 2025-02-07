import os #dosya okuma işlemleri için kullanılan kütüphane import edilmesi gerekir
import glob#dosyaları isimlerini kullanabilmek için glob import edilir
from ders10 import dosyayolu #burasi önemli 
dosyaOku=open(dosyayolu(),"r")
print(dosyaOku.read())

dosyaOku.close()