import urllib.parse
import urllib.request

try:
    size = input("entry a size value : ")
    data = input("entry a data : ")
    datas = {
        "size": size,
        "data": data
    }
    datas = urllib.parse.urlencode(datas)
    api_url = "https://api.qrserver.com/v1/create-qr-code/?" + datas
    file_name = ".\\QR" + data + ".png"
    urllib.request.urlretrieve(api_url, file_name)
    print("download success")

except:
    print("error")
