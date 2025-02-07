import urllib.request
import urllib.parse
import re

site_url = "https://httpbin.org/"  # SERVER (SUNUCU)
html = urllib.request.urlopen(site_url)  # sayfaya istek (request) atar ve siteye bağlanır.
print(html)
print(html.read())  # belirtilen sayfanın html kodlarını getirir.

'''
header bilgisi gönderme : bazı sitelere kolay erişebilirken bazı sitelere ise güvenlik için erişemiyoruz
bunun için user agent içinde tanımlı olan işletim sistemi , tarayıcı ve cihaz bilgileri header bilgisiyle
birlikte siteye göndermemiz gerekebilir. 
'''

url_site = "https://eksisozluk.com/"
header_info = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
    # internetten ulaşılabilir.
}
request1 = urllib.request.Request(url_site, headers=header_info)
html1 = urllib.request.urlopen(request1)
print(html1.read())

'''   sitelere veri gönderme  '''

data = {
    "username": "burakcnaksy",
    "password": "1234567",
    "email": "aksoyburak808@gmail.com",
    "phone": "05350482874",
    "department": "computer engineering"
}
password_data = urllib.parse.urlencode(data)  # burda kendi verilerimizi yollamak için önce şifrelememiz gerekiyor.
print(password_data)

'''     
get metodu ile veri gönderme     
gönderilen veriler url yapısı ile birleştirilir. yani url üzerinde saklanır ve url üzerinde gözükür
sadece yazı formatında veriler gönderebiliriz.sitenin url yapısı ve gönderdiğimiz veriler birbirinden
? ile ayrılır.
'''

site_url = "https://httpbin.org/get"
data = {
    "username": "burakcnaksy",
    "password": "1234567",
    "email": "aksoyburak808@gmail.com",
    "phone": "05350482874",
    "department": "computer engineering"
}
password_data = urllib.parse.urlencode(data)
end_site_url = site_url + "?" + password_data
html2 = urllib.request.urlopen(end_site_url)
print(html2.read())

'''
post metodu ile veri gönderme 
gönderilen veriler url yapısı ile birleştirilmez , yani url üzerinde saklanmaz ve url üzerinde gözükmez.
sadece yazı formatında veriler değil, resim ,ses dosya gibi farklı türde veriyi post metodu ile gönderebiliriz.
'''

site_url = "https://httpbin.org/post"
data = {
    "username": "burakcnaksy",
    "password": "1234567",
    "email": "aksoyburak808@gmail.com",
    "phone": "05350482874",
    "department": "computer engineering"
}
password_data = urllib.parse.urlencode(data)  # string objesi.
password_data = password_data.encode("utf-8")  # bayt objesine dönüştürür.

req1 = urllib.request.Request(site_url, data=password_data)  # data bayt cinsinden olmak zorundadır
html3 = urllib.request.urlopen(req1)
print(html3.read())

'''
html etiketlere göre içerik ayırma
'''
site_url = "https://www.sondakika.com/"
html5 = urllib.request.urlopen(site_url)
cont = str(html5.read())
content = "<title>(.*?)</title>"
search_result = re.search(content, cont)
if search_result:
    label = search_result.group(0)
    content = search_result.group(1)

    print("label is :", label)
    print("contents is : ", content)

'''
dosya indirme işlemi
'''

image_url = "https://images.unsplash.com/photo-1738363436637-ee6f4a910715?q=80&w=1965&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
urllib.request.urlretrieve(image_url, ".\\image1.png")  # mevcut pathe verilen isimle indirme işlemini yapar.
