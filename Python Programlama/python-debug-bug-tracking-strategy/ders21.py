import logging

liste = [1, 2, 3]
try:
    eleman = liste[5]  # Hata: İndeks 5, listenin boyutundan büyük
    print("Liste elemanı:", eleman)
except Exception as e:
    print("Hata: Geçersiz indeks :", e)

# Logları ekrana yazdıralım    
logging.basicConfig(level=logging.DEBUG)

# Logları dosyaya da kaydedelim
logging.basicConfig(filename='app.log', level=logging.DEBUG)

# Log düzeylerine göre mesajlar
logging.debug("Bu bir hata ayıklama mesajıdır.")
logging.info("Bu bir bilgi mesajıdır.")
logging.warning("Bu bir uyarı mesajıdır.")
logging.error("Bu bir hata mesajıdır.")
logging.critical("Bu bir kritik hata mesajıdır.")