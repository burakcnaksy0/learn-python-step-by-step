from ITasit import *
import time
class Bisiklet(TasitAraciArayuzu):
    def hareket_et(self):
        time.sleep(1.6)
        print("Pedallar çevriliyor...")
        
    def hizlan(self):
        time.sleep(1.6)
        print("Bisiklet vitesi arttirildi hizlaniyor...")
    
    def yavasla(self):
        time.sleep(1.6)
        print("Bisiklet vitesi dusuruldu yavasliyor...")
        
    def dur(self):
        time.sleep(1.6)
        print("Bisiklet durdu.")
