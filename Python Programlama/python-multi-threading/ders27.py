import threading
import requests
import time
def fetch_url(url):
    response = requests.get(url)
    print(f"{url}: {response.status_code}")

urls = [
    'https://www.example.com',
    'https://www.python.org',
    'https://www.github.com',
]

threads = []

for url in urls:
    thread = threading.Thread(target=fetch_url, args=(url,))
    threads.append(thread)
    thread.start()
    time.sleep(0.8)

for thread in threads:
    thread.join()

print("Tüm URL'ler çekildi!")
