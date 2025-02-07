#  uygulama


names = ['ali', 'hakan', 'yağmur', 'deniz']
years = [1998, 2000, 1998, 1987]

names.append('cenk')
print(names)

names.insert(0, 'sena')
print(names)

val = names.index('deniz')
print(val)

# pop indeks , remove karakteri ister..

names.remove('deniz')
print(names)

result = 'ali' in names
print(result)

# str = 'dacia','audi' karakter dizisini listeye çevirme

str = "dacia,audi"
result = str.split(',')
print(result)


markalar = []
marka = input("marka giriniz : ")
markalar.append(marka)
marka = input("marka giriniz : ")
markalar.append(marka)
marka = input("marka giriniz : ")
markalar.append(marka)
print(markalar)
