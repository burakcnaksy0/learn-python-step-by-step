'''
Fonksiyon dışarıdan bir cümle alacak ve bir kelimedeki ortalama karakter sayısını return edecek.

ortalama karakter sayısı= toplam karakter / toplam kelime şeklinde hesaplayabilirsiniz

kelimeSayısı = boşlukSayısı + 1

'''


def averageCharacter(cümle):
    count = 0
    letterList = list(cümle)

    for i in range(len(letterList)):
        if letterList[i] == ' ':
            count += 1

    return len(letterList)/(count+1)


print("result is {}".format(averageCharacter("toplam kelime şeklinde hesaplayabilirsiniz")))
