from datetime import datetime
import time

print(datetime.now())

now = datetime.now()
clsnow = datetime.ctime(now)
print(clsnow)

strftim = datetime.strftime(now, "%X")  # saatbilgisi
strftim1 = datetime.strftime(now, "%D")  # günbilgisi
strftim2 = datetime.strftime(now, "%A")  # günisimbilgisi
strftim3 = datetime.strftime(now, "%B")  # aybilgisi
strftim4 = datetime.strftime(now, "%Y")  # yılbilgisi

print(strftim)
print(strftim1)
print(strftim2)
print(strftim3)
print(strftim4)

print("before sleeping")
time.sleep(5)  # programın belirtile süre(saniye cinsinden) kadar beklemesini (uyumasını) sağlar.
print("yeahh!I wake up")
