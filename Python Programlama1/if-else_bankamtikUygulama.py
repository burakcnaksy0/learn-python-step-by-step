# if-else_bankamatikUygulama

kullanıcıBakiyesi, günlükLimit = 1250, 450
girişEkranMetni = '''

ATM mize hoşgeldiniz.

1. para çekmek için = 1
2. para yatırmak için = 2
3. bakiye görüntülemek için = 3
4. çıkış = 4
'''
print(girişEkranMetni)
yapılacakİşlem = input("işleminizi seçiniz : ")

if yapılacakİşlem == '1' or yapılacakİşlem == '2' or yapılacakİşlem == '3' or yapılacakİşlem == '4':
    if yapılacakİşlem == '1':
        cekilenMiktar = int(input("çekilecek miktar : "))
        if cekilenMiktar <= günlükLimit:
            kullanıcıBakiyesi -= cekilenMiktar
            print("bakiye : {}".format(kullanıcıBakiyesi))
        else:
            print("hatalı giriş!!!")
    elif yapılacakİşlem == '2':
        yatırılıcakBakiye = int(input("yatırmak istediğiniz miktar :"))
        kullanıcıBakiyesi += yatırılıcakBakiye
        print("bakiye : {}".format(kullanıcıBakiyesi))
    elif yapılacakİşlem == '3':
        print(" bakiye : {}".format(kullanıcıBakiyesi))    
    elif yapılacakİşlem == '4':
        breakpoint
    else:
        print("güncel bakiyeniz :{} ".format(kullanıcıBakiyesi))
else:
    print("yanlış işlem !! lütfen tekrar deneyiniz..")
