x = (int(input("bir değer giriniz : ")))

'''

result = 1
for i in range(1, x+1):
    result *= i
    i -= 1
print("Result : {}".format(result))

'''

i=1
value=1

while i<=x:
    value*=i
    i +=1
print("result is {} " .format(value))    