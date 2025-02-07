# ünlü harf calculater


def letterCalculate(kelime):
    count = 0

    list1 = list(kelime)
    for i in range(len(list1)):

        if list1[i] == 'a' or list1[i] == 'e' or list1[i] == 'ı' or list1[i] == 'i' or list1[i] == 'o' or list1[i] == 'ö' or list1[i] == 'u' or list1[i] == 'ü' or list1[i] == 'A' or list1[i] == 'E' or list1[i] == 'I' or list1[i] == 'İ' or list1[i] == 'O' or list1[i] == 'Ö' or list1[i] == 'U' or list1[i] == 'Ü':

            count += 1

    return count


print(letterCalculate("burakcan"))
print(letterCalculate("ünlü harf hesaplama"))
print(letterCalculate("Bu Kurs Hakkında"))
print(letterCalculate("Ödev Soruları"))
