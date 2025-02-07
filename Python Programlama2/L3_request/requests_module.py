import requests

'''
get metodu ile gönderme
'''

site_url = "https://httpbin.org/get"
response = requests.get(site_url)
print(response)
print(response.status_code)  # sayfaya gönderilen isteğin durum kodunu verir. 200:OK,..
print(response.content)  # sayfa içeriğini gösterir
print()

paramater = {
    "usename": "burakcnaksy",
    "password": "14940600"
}
response1 = requests.get(site_url, params=paramater)
print(response1)
print(response1.content)
print(response1.url)
print()

'''
post metodu sayfanın içeriğini alma ve data gönderme
'''

page_url = "https://httpbin.org/post"
resp = requests.post(page_url)
print(resp)
print()

resp1 = requests.post(page_url, data=paramater)
print(resp1)
print(resp1.url)
print(resp1.headers)
print(resp1.request)    # yapılan isteğin ne olduğunu gösterir ?
print(resp1.elapsed)    # gönderilen istekten ve alınan cevaba kadar geçen süre.
