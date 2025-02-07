#Fonksiyonlarda Scope Kavrami ?
#Scope 2 kisimda incelenir Global Scope ve Local Scope

#Global Scope Nedir?
#fonksiyon disindan tanimlanan degiskenler global scope olarak isimlendirilir

#Local Scope Nedir?
#fonksiyon icinde tanimlanan degiskenlerdir ve sadece o fonksiyon icinden erisim saglanir

#ornek1 Global ve Local Scope Farklari Nelerdir

x=10

def my_function():
    x=5
    print("Fonksiyon icindeki x:",x)

my_function()

print("Fonksiyon disindaki x:",x)


#ornek2 Global Degiskenin Fonksiyon icinde kullanimi
y=20

def another_function():
    global y
    y=15
    print("Fonksiyon icindeki y:",y)

another_function()
print("Fonksiyon disindaki y:",y)