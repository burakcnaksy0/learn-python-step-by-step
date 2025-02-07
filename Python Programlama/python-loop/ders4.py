#Pythonda'da Donguler

#belirli bir koşul veya aralık içinde
#birden fazla kez çalışmasını sağlayan yapılardır.

#for dongusu
futbolcu_listesi=["arda","emre","oguz","kubilay","arif"]

for futbolcu in futbolcu_listesi:
    print("Futbolcunun Adi:",futbolcu)


for index in range(0,10,1):
    print(index+1)


#while dongusu
sayac=1

while sayac<100:
    print(sayac)
    sayac = sayac + 2

kontrolSayaci=1
while kontrolSayaci<10:
    if kontrolSayaci == 3:
        print("dongudeki bu deger atlanacak !")
        kontrolSayaci +=1
        continue
    elif kontrolSayaci == 7:
        print("dongu burada iptal edildi !")
        break
    
    print(kontrolSayaci)
    kontrolSayaci += 1            