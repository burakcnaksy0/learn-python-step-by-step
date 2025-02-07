import numpy as np

# 1 ile 10 arasında rastgele sayılardan oluşan bir NumPy dizisi oluşturun
random_array = np.random.randint(1, 11, size=(5, 5))

# Dizinin toplamını, ortalama değerini ve en büyük değerini yazdırın
print("Dizi:")
print(random_array)
print("Toplam:", np.sum(random_array))
print("Ortalama:", np.mean(random_array))
print("En Büyük Değer:", np.max(random_array))