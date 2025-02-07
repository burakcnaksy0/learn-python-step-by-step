# math metodları
import math

# mutlak değer hesaplama abs()

x = -5
print(abs(x))


# sayı yuvarlama

'''
ceil() : ondalıklı kısmı buluna sayıyı bir üstteki tam sayıya yuvarlamak.
floor() : ondalıklı kısmı buluna sayıyı bir alttaki tam sayıya yuvarlamak.
round() : ondalıklı kısmı 0.5 ten büyükse üst, küçükse alttakine yuvarlar.

import math edilmelidir.

'''

x = 1.35
y = 3.95

print(math.ceil(x), math.ceil(y))

print(math.floor(x), math.floor(y))

print(round(x), round(y))


# üs alma

print(math.pow(2, 3))
print(math.pow(3, 2))


# kök alma

print(math.sqrt(81))
print(math.sqrt(15))


# ikili tabana dönüştürme

print(bin(5))
print(bin(20))
print(bin(45))
'''

def alt_kumeler(kume):
    if len(kume) == 0:
        return [[]]
    alt_kume = alt_kumeler(kume[1:])
    return alt_kume + [[kume[0]] + x for x in alt_kume]

kume = {1, 2, 3,4,5,6,7}
alt_kumeler = alt_kumeler(list(kume))

print("Kümenin Alt Kümeleri:")
for alt_kume in alt_kumeler:
    print(set(alt_kume))
'''