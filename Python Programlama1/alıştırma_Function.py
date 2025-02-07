def harfDeğiştir(cumle, eski, yeni):
    cumle = list(cumle)
    for letter in range(len(cumle)):
        if cumle[letter] == eski:
            cumle[letter] = yeni
        return cumle


cümle = input("bir cümle giriniz :")
eskiHarf = input("eski harfi giriniz :")
yeniHarf = input("yeni harfi giriniz :")
yeniCumle = str(harfDeğiştir(cümle, eskiHarf, yeniHarf))
print(yeniCumle)
