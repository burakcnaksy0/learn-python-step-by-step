# if-elif-else bloğu
import random





sayı1 = random.randint(1, 5)
sayı2 = random.randint(1, 5)
print("1. sayı {} sayısına eşittir".format(sayı1))
print("2.sayı {} sayısına eşittir.".format(sayı2))


if sayı1 > sayı2:
    print("{} sayısı {} sayısından daha büyüktür.".format(sayı1, sayı2))

elif sayı1 == sayı2:
    print("{} ve {} sayısı birbirine eşittir.".format(sayı1,sayı2))

else:
    print("{} sayısı {} sayısından daha büyüktür.".format(sayı2, sayı1))
