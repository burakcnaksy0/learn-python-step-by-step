import os

print(os.sep)  # dosyaların ne ile ayrıldığı
print(os.getcwd())  # o an modülün içinde bulunduğu dosya dizinini verir.
os.chdir(r'C:\Users\burak\OneDrive\Masaüstü')  # modülün bulunduğu dizini değiştirir.
print(os.getcwd())
print(os.listdir())  # dizin içindeki dosya ve klasörleri liste yapısı halinde sunra.
os.startfile('ses.txt')  # verilen dosya dizinindeki veya dosya adını açma
os.startfile('.')  # an bulunan dizini açma
os.mkdir(r'C:\Users\burak\OneDrive\Masaüstü\as')  # verilen dizinde ve verilen isimde dosya açar.
os.makedirs(r'C:\Users\burak\OneDrive\Masaüstü\sa\hello\world')  # verilen dizinde ve verilen isimde dosya açar.
print(os.path.abspath('ses.txt'))  # içerisine verdiğimiz dosyanın tam yolunu verir.
print(os.path.exists(os.path.abspath("ses.txt")))  # içine girilen dosya veya dizinin olup olmadığını kontrol eder.
