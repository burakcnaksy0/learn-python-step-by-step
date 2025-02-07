import requests
from bs4 import BeautifulSoup

page_url = "https://www.isbank.com.tr/doviz-kurlari"
response = requests.get(page_url)
if response.status_code == 200:
    html_content = response.content
    soap = BeautifulSoup(html_content, "html.parser")
    print(soap.prettify())

else:
    print("hata")
