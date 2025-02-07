'''
iterator (yineleyici) : sayılabilir sayıda değer içeren bir nesnedir -> iter ve next fonksiyonları.
'''

myList = ["c", "c++", "python"]
myIt = iter(myList)

while True:
    try:
        print(next(myIt))
    except:
        break


class Number():
    def __iter__(self):
        self.number = 0
        return self

    def __next__(self):
        temp = self.number
        self.number += 1
        return temp

n1 = Number()
number = iter(n1)

print(next(number))
print(next(number))
print(next(number))
print(next(number))
print(next(number))

class Counter:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self  # Iterator nesnesini döndürür

    def __next__(self):
        if self.current > self.end:
            raise StopIteration  # Bittiğinde hata fırlatır
        value = self.current
        self.current += 1
        return value

counter = Counter(1, 5)

for num in counter:
    print(num)  # 1, 2, 3, 4, 5
