from bs4 import BeautifulSoup
import requests

'''
html içeriğini çektiğimiz web siteyi parçalamak için kullanıyoruz.
'''

'''
<a> Bir link oluşturmamızı sağlar

<article> Bir makale oluşturmamızı sağlar

<b> Kalın metin oluşturmamızı sağlar

<br> Bir sonraki satıra geçmemizi sağlar

<button> Buton oluşturmamızı sağlar

<div> Yeni bir bölüm oluşturmamızı sağlar

<footer> Alt bilgi oluşturmamızı sağlar

<form> Kullanıcı girişi için bir HTML formu oluşturmamızı sağlar

<h1> .. <h6> Başlık oluşturmamızı sağlar, h1 en büyük ve önemli h6 en küçük ve önemsiz başlık için kullanılabilir.

<img> Bir görüntü oluşturmamızı sağlar

<input> Bir giriş kontrolü oluşturmamızı sağlar

<label> Bir <input> öğesi için bir etiket oluşturmamızı sağlar

<li> Bir liste öğesi oluşturmamızı sağlar

<ol> Sıralı liste oluşturmamızı sağlar

<p> Bir paragraf oluşturmamızı sağlar

<strong> Önemli metni vurgulamamızı sağlar

<table> Tablo oluşturmamızı sağlar

<td> Bir tablodaki bir hücreyi oluşturmamızı sağlar

<th> Bir tabloda, bir başlık hücreyi oluşturmamızı sağlar

<title> Belge için bir başlık oluşturmamızı sağlar

<tr> Bir tabloda, bir satır oluşturmamızı sağlar

<ul> Sırasız liste oluşturmamızı sağlar
'''

page_url = "https://www.sondakika.com/"
response = requests.get(page_url)
if response.status_code == 200:
    html_content = response.content
    soup = BeautifulSoup(html_content, "html.parser")
    # print(soup.prettify())
    # print(soup.find("title").text)    # belirtilen etiketler arasındaki bilgileri bulur.
    for i in soup.find_all("a"):  # belirtilen etikete ait bütün değerleri getirir.
        # print(i.text)
        print(i.get("title"))
