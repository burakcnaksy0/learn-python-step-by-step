# verilen sayının tam bölenlerini bulma
'''


def f1(integer):
    for i in range(1,integer+1):
        if integer % i == 0:
            print(i)

f1(n)
'''
#recursıve faktorıyel
n = int(input("enrty a value :"))
def fac(n):
    if n == 0 :
        return 1
    else:
        return n*fac(n-1)


print(fac(n))