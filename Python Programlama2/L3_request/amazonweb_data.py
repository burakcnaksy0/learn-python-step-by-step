'''
amazon en çok satanlar listesi içeriğini alma
'''
import requests
from bs4 import BeautifulSoup

page_url = "https://www.amazon.com.tr/gp/bestsellers/books"
response = requests.get(page_url)
if response.status_code == 200:
    html_content = response.content
    soup = BeautifulSoup(html_content, "html.parser")
    for i in soup.find_all("li"):
        print(i)
else:
    print("error")
