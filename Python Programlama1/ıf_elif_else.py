# if else yapıları
sayı1 = int(input("entry a value  :"))
sayı2 = int(input("entry a value  :"))

if sayı1>sayı2:
    print("{} , {} den büyüktür .".format(sayı1,sayı2))

elif sayı1<sayı2:
    print("{} , {} den küçüktür .".format(sayı1,sayı2))
else:
    print("{} ve {} eşittir .".format(sayı1,sayı2))


# tek çift sorgulama

sayı3 = int(input("entry a value  :"))

if sayı3%2 ==1:
    print("{} is odd.".format(sayı3))
else:
    print("{} is even.".format(sayı3))

# positive or negative

sayı4 = int(input("entry a value  :"))

if sayı4<0:
    print("{} is negative".format(sayı4))
elif sayı4>0:
    print("{} is positive".format(sayı4))
else:
    print("{} is zero".format(sayı4))


