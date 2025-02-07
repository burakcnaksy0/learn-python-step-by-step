# kaçış ifadeleri

# break => herhangi bir koşula göre döngüyü sonlandırmak için kullanılan anahatar kelime
# continue =>  herhangi bir koşula göre döngünün iterasyonun sonlandırmak ve bir sonraki iterasyona geçmek için kullanilan anahtar keilimedir
# pass =>  herhangi bir koşula göre pass anahtar kelimesinin kullanıldıgı koşulun atlanması için kullanılan anahtar kelime

i = 0
while True:
    print(i, end=(" "))
    if i >= 50:
        print("\nDöngüyü sonlandıryom")
        break
    i += 2

print("\n")

for i in range(100):
    if not i % 5 == 0:
        continue   # başa döndürür
    print(i, end=(" "))

print("\n")

for i in range(100):
    if not i % 5 == 0:
        pass   # bu satırı atlar
    print(i, end=(" "))
