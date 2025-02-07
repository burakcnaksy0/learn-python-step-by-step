#kullanicidan bir sayi girmesini isteyelim
sayi=int(input("Bir sayi giriniz:"))

#girilen sayi cift mi ? tek mi ?
if sayi % 2 == 0:
    print(f"{sayi} bir cift sayidir!")
else:
    print(f"{sayi} bir tek sayidir!")    