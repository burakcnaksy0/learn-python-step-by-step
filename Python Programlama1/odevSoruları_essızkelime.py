# her karakter bir kere sayılacak ve eşsiz karakterlerin sayısını return edecek.

'''
burak 5 eşsiz karakter
çanak 4 eşsiz karakter


'''


def essizKarakter(string):
    harfList = []
    for ch in string:
        if ch not in harfList:
            harfList.append(ch)
    print(harfList)
    return len(harfList)

print("{} tane eşsiz karakter vardır.".format(essizKarakter("burakcan")))