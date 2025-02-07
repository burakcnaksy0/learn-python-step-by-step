# döngüyle listeye erişmek

array = [2, 45, 123, 768, 123, 754, 213, 54, 214, 34]


array[9] = 343

for eleman in array:
    print(eleman)


numberOfElement = len(array)
print("Element number : {}".format(numberOfElement))


for i in range(len(array)):        # indekslere erişmek için kullanılır.
    print(array[i])


list = [1, 2, 3, 4, 5, 6, 7]

for i in range(len(list)):
    list[i] = i**2
print(list)


# listeye eleman eklemek

'''
append : listenin sonuna eklemek için kullanılır.
insert : listenin belirtilen indeksine eklemek için kullanılır.

'''

list.append(4)
list.insert(0, 5)   # (indeks,verilen)
print(list)


# listeden eleman silme

'''
remove : listeden belirtilen değeri çıkartmak için kullanılır.
delete : listenin belirtilen indeksinden bir değer silmek veya listeyi komple silmek için kullanılır.
pop : listenin son elemanını veya istenilen indeksteki elemanı silmeyi ve sildiğimiz elemanı başka bir değişkene atmak için kullanılır.

'''

liste = [1, 2, 3, 4, 5, 6, 7]

liste.remove(2)
del (liste[0])
x = liste.pop()

print(liste)
print(x)


# listede eleman kontrolü

'''
in : eğer ki eleman liste içinde varsa true yoksa false değeri döndürür.
not in : eğer ki eleman liste içinde varsa false , yoksa true değeri döndürür.
index : aradğımız eleman eğerki listede varsa bulundugu indeksi verir, yoksa value error verir.

'''

liste1 = [1, 2, 3, 4, 5, 6, 7, 8]

print(2 in liste1)
print(12 in liste1)

print(3 not in liste1)
print(20 not in liste1)

print(liste1.index(2))


# listeyi sıralama

'''
sort : listeyi küçükten büyüğe sıralar.
reverse : listenin elemanlarını ters çevirir.

'''

ls = [21, 643, 123, 234, 685, 323, 65, 213, 654, 123, 53, 34, 6]
ls.sort()
print(ls)

ls.reverse()
print(ls)


# listede bir elemanın kaç kere geçtıgını bulma

la = [1, 1, 1, 2, 3, 5, 2, 4, 7, 2, 1, 4, 6]

print(la.count(1))


sum = 0
for i in range(len(la)):
    sum += la[i]

print(sum)



# liste eleman üretme yöntemleri

b1 = [i for i in range(5)]
print(b1)

b2 = [2*i**2 for i in range(5)]
print(b2)

b3 = [i**2 for i in range(5) if i % 2 == 0]
print(b3)
