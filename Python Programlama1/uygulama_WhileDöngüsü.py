
sayılar = [1, 3, 5, 7, 9, 12, 19, 21]
length = len(sayılar)

while length-1 >= 0:
    print(sayılar[length-1], end=(" "))
    length -= 1


başlangıç = int(input("\nbir değer giriniz :"))
son = int(input("bir değer giriniz :"))

while başlangıç <= son:
    if başlangıç % 2 == 1:
        print(başlangıç, end=(" "))
    başlangıç += 1

list = []
j = 0
while j < 5:
    number = int(input("bir sayı giriniz : "))
    list.append(number)
    j += 1

print(list)
