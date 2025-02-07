import random

print(random.random())  # 0 - 1 arasında random değerler
print(random.uniform(0.5, 5.5))  # kendi verdiğin aralıklarda ondalıklı sayı döndürür
print(random.randint(4, 31))  # kendi verdiğin aralıklarda tam sayı döndürür

list_name = ["burak", "ceren", "berat", "irem"]
list_surname = ["alkan", "aksoy", "yılmaz", "kaya"]

random_name = random.choice(list_name)  # rastgele bir eleman seçer
random_surname = random.choice(list_surname)

full_name = str(random_name) + " " + str(random_surname)
print(full_name)

random.shuffle(list_name)  # listeyi karıştırır
print(list_name)

print(random.sample(list_name,2))   # listeden rastgele girilen değer kada seçim yapar