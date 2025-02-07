import json

data = {'Ad': 'Ahmet', 'Soyad': 'Yılmaz', 'Yaş': 25}

with open('dosya.json', 'w') as file:
    json.dump(data, file)