# if-else_hesapMakinesiUygulama

işlemler = '''

 1.toplama: '+'
 2.çıkarma: '-'
 3.çarpma: '*'
 4.bölme: '/'
 5.üs alma: '^'
 6.mod alma: '%'

'''
print(işlemler)
yapılacakSeçim = input("bir işlem seçiniz : ")


if yapılacakSeçim == '1' or yapılacakSeçim == '-' or yapılacakSeçim == '*' or yapılacakSeçim == '/' or yapılacakSeçim == '^' or yapılacakSeçim == '%':
    sayı1 = int(input("sayı giriniz :"))
    sayı2 = int(input("sayı giriniz :"))
if yapılacakSeçim == '1':
    print(sayı1+sayı2)
elif yapılacakSeçim == '-':
    print(sayı1-sayı2)
elif yapılacakSeçim == '*':
    print(sayı1*sayı2)
elif yapılacakSeçim == '/':
    print(sayı1/sayı2)
elif yapılacakSeçim == '^':
    print(sayı1**sayı2)
elif yapılacakSeçim == '%':
    print(sayı1 % sayı2)


else:
    print("işlem hatalı")
