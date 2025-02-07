# en büyük ve en küçük n. sayıyı return eder.

def listValue(number):

    liste = [2, 5, 1, 3, 4, 7, 6, 8]
    liste.sort()
    maxValue = liste[number-1]
    minValue = liste[-number]
    print(liste)

    return maxValue, minValue


value = int(input("enrty a value : "))
print("listedeki {}. büyük ve küçük sayılar : {}".format(value, listValue(value)))
 