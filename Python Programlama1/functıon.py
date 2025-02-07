# fonksiyonlar

'''
metodlar:
  1: normal
  2: parametreli
  3: returnlu
'''

n = int(input(" entry a value "))
m = int(input(" entry a value "))
def sum(x,y):
    print(x+y)
sum(n,m)

# calculater

def calculate(islem):
    if islem==1:
        n = int(input("entry a value "))
        m = int(input("entry a value "))
        sum=m+n
        return print(sum)
    elif islem==2:
        n = int(input("entry a value "))
        m = int(input("entry a value "))
        result=m-n
        return print(result)
    else:
        print("fail choose")
y = int(input("what is your number :"))
calculate(y)





