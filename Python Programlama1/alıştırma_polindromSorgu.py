# polindrom string

# tersi ve düzü bribiryle aynı olan kelime veya sayılardır.


def polindromSorgu(kelime):
    ters = kelime[::-1]
    if ters != kelime:
        return False
    return True


print(polindromSorgu("akkk"))
print(polindromSorgu("ece"))


'''
def sorgu(kelime):
    list1 = list(kelime)
    tempList = list1
    tempList[::-1]
    for i in range(len(tempList)):
        if tempList != list1:
            return False
        return True
    

print(sorgu("kara"))
print(sorgu("ece"))
'''
