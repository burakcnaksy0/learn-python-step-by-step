from ITasit import *
import time
class Araba(TasitAraciArayuzu):
     def hareket_et(self):
        time.sleep(1.6)
        print("araba motoru çalistiriliyor...")
        
     def hizlan(self):
        time.sleep(1.6) 
        print("Araba vitesi arttirildi hizlaniyor...")
    
     def yavasla(self):
        time.sleep(1.6) 
        print("Araba vitesi dusuruldu yavasliyor...")
        
     def dur(self):
        time.sleep(1.6) 
        print("Araba durdu.")   