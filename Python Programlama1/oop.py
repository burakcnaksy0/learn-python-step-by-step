'''
class name():
   '''


class employee():
    def __init__(self):      # self komutu verilen değerlerin biribirine karısmaması ıcın kullanılır.
        self.unvan: ''             # her seyin kendine özgü kalması birbirinin üzerine eklenmemesini sağlar
        self.language = []
        self.name = ''
        self.surname = ''
        self.age = None

sy = employee()
sy.unvan='it'
sy.language.append('c')
sy.language.append('java')
sy.language.append('python')
sy.age=22
sy.name='burak'
sy.surname='aksoy'

print(sy.language)

ys=employee()
ys.unvan='bebek'
ys.language.append('autocad')
ys.age=22
ys.name='ceren'
ys.surname='aksoy'

print(ys.language)