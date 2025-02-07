# liste metotları

numbers = [1, 10, 4, 7, 2, 4, 4, 10, 6, 3]
letters = ['a', 'h', 'j', 'a', 'k', 'r', 'q', 'b', 'c', 'i', 'z', 't']

value = min(numbers)
print(value)
value = max(numbers)
print(value)

value = min(letters)
print(value)
value = max(letters)
print(value)


val = numbers[3:6]       # 3 ü alır ama 6 yı almaz.
print(val)

numbers.append(42)       # listenin sonuna ekleme yapar.
print(numbers)

numbers.insert(3, 77)    # istenilen indeksten önce ekleme yapar.
print(numbers)

numbers.pop()            # sondaki veya istenilen indeksi siler
numbers.pop(2)
print(numbers)


numbers.remove(1)        # girilen karakter dizide varsa onu kaldırır.
print(numbers)

numbers.sort()           # büyükten küçüğe sıralar.
print(numbers)

letters.sort()           # alfabetik sıralama yapar.
print(letters)

numbers.reverse()        # diziyi ters çevirir.
print(numbers)

val = letters.count('a')  # girilen değerden kaç tane oldugunu söyler.
print(val)


