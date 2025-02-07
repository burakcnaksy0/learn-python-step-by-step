# dictionary uygulaması

students = {

    '714': {
        'name': 'burak',
        'surname': 'aksoy',
        'no': 714,
        'phone': 3254572
    },
    '808': {
        'name': 'berat',
        'surname': 'aksoy',
        'no': 808,
        'phone': 5432456
    }
}

print(students['714'])
print(students['808'])


# kullanıcadan alıpda yap !!!!


ogrenciler = {}


okulNo = input('okul no : ')
name = input('isim :')
surname = input('soyad :')
phoneNumber = input('telNo :')

ogrenciler[okulNo] = {
    'isim': name,
    'soyad': surname,
    'okulNo': okulNo,
    'phone': phoneNumber
}

print(ogrenciler)
