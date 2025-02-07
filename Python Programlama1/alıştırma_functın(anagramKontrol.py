# anagram kontrol 1 kelimenin harfleri yerdeğiştirmesiyle anlamlı bir kelime oluşturma

# kalem,kelam

def anagramKontrol(kelime1, kelime2):
    if len(kelime1) != len(kelime2):
        return False
    kelime1list = list(kelime1)
    kelime2list = list(kelime2)
    kelime1list.sort()
    kelime2list.sort()

    for i in range(len(kelime1list)):
        if kelime1list[i] != kelime2list[i]:
            return False
    return True


print(anagramKontrol("kelam", "kalem"))
print(anagramKontrol("burak", "can"))
