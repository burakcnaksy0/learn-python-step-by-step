import sched
import time

#zamanlayici olusturalim
s=sched.scheduler(time.time,time.sleep)

#arkaplan temizligi icin bir fonksiyon olusturalim

def arkaplan_temizleyici():
    print("Arkaplan temizleyici calisiyor...")
    s.enter(5,1,arkaplan_temizleyici)

s.enter(5,1,arkaplan_temizleyici)#5 sn'de bir calismasini sagliyoruz
s.run()# zamanlayiciyi baslatalim ve bellekteki arkaplan temizligi aktiflessin
    