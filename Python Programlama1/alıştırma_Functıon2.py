def buyukHarf(cumle):
    cumle = list(cumle)
    cumle[0] = cumle[0].upper()
    for i in range(len(cumle)):
        if cumle[i] == '.':
            if i+1 == len(cumle):
                return cumle
            i += 1
            cumle[i] = cumle[i].upper()
    return cumle


metin = input("bir metin giriniz :")

text = str(buyukHarf(metin))
print(text)
