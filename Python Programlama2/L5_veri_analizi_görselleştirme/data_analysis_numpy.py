import numpy as np

num_lists = np.array([1, 2, 3, 4, 5])
print(type(num_lists))
print(num_lists)

npZeroArray = np.zeros((5, 5), dtype="int")  # tüm elemanları 0 olan array -> 2D boyutlu
print(type(npZeroArray))
print(npZeroArray)

npOnesArray = np.ones((5, 5), dtype="int")  # tüm elemanları 1 olan array -> 2D boyutlu
print(type(npOnesArray))
print(npOnesArray)

npFullArray = np.full((5, 5), 7)  # tüm elemanları verilen değer olan array -> 2D boyutlu
print(type(npFullArray))
print(npFullArray)

npArangeArray = np.arange(0, 50, 5)  # başlangıç , bitiş ve sabit artış değeri olan array
print(type(npArangeArray))
print(npArangeArray)

npLinSpaceArray = np.linspace(0, 50, 10)  # başlangıç - bitiş arasını belirtilen n eşit parçaya böler.
print(type(npLinSpaceArray))
print(npLinSpaceArray)

npRandomArray = np.random.randint(0, 50, (5, 5))  # verilen boyutta verilen değerler arasında random değerler atanır.
print(type(npRandomArray))
print(npRandomArray)

'''
2 boyutlu arrayde en büyük değeri bulma
max_value = npRandomArray[0, 0]   
for row in npRandomArray:
    for value in row:
        if value > max_value:
            max_value = value
print(max_value)

2 boyutlu arrayde en küçük değeri bulma
min_value = npRandomArray[0, 0]
for row in npRandomArray:
    for value in row:
        if value < min_value:
            min_value = value
print(min_value)

'''
'''
NUMPY ARRAY BİLGİLERİ
dtype: arraydeli verilerin eleman tipi
size : arraydeki toplam eleman sayısı
ndim : arrayin boyut sayısı
shape : arrayin satır-sütun bilgisi
'''
print(npRandomArray.dtype)
print(npRandomArray.size)
print(npRandomArray.ndim)
print(npRandomArray.shape)

'''
hazır fonksiyonlar:
reshape : arrayı yeniden boyutlandırır.
concatenate : np arraylari birleştirmek için kullanılır.
split : arrayleri bölmek ve ayırmak için kullanılır.
srt : arrayleri sıralamak için kullanılır.
'''
nparray = np.arange(1, 10)
print(nparray)
nparray2d = nparray.reshape((3, 3))  # nparray.reshape((satır,sütün))
print(nparray2d)

a = np.arange(1, 10)
b = np.arange(10, 19)
c = np.concatenate([a, b])
print(c)

x, y, z = np.split(c, 3)
print(x)
print(y)
print(z)
print("*******************")
npArray2D = np.random.randint(0, 50, (4, 4))
x1, y1 = np.vsplit(npArray2D, [2])
print(npArray2D)
print(x1)
print(y1)
print("*******************")

x2, y2 = np.hsplit(npArray2D, [2])
print(x2)
print(y2)
print("*******************")

npSortedArray = np.sort(
    npArray2D)  # axis=0 sütun(alt alta) sıralaması  yapar   axis=1 satır(yan yana) sıralaması  yapar
print(npSortedArray)
