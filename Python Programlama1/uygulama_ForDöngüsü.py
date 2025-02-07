sayılar = [1, 3, 5, 7, 9, 12, 19, 21]

for i in sayılar:
    if i % 3 == 0:
        print("", i, end=(" "))

sum = 0
for i in sayılar:
    sum += i

print("\n", sum)

toplam = 0
for i in sayılar:
    if i % 2 == 1:
        toplam += i**2
print("", toplam)


sehirler = ['kocaeli', 'istanbul', 'ankara', 'izmir', 'rize', 'trabzon']
