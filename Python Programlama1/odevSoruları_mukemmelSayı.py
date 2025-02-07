# mukemmel sayı

# mukemmel sayı kendi dısındaki bölenlerinin toplamı aynı sayıyı vericek.
# 6 = 1,2,3
number = int(input(" bir sayı giriniz : "))

result = 0
for i in range(1, number):
    if number % i == 0:
        result = result+i


if result == number:
    print(" {} bir mükemmel sayıdır.".format(number))
else:
    print(" {} bir mükemmel sayı değildir.".format(number))


'''

# belli bir aralıktaki mükemmel sayılar

number = int(input(" bir sayı girniz :"))
sum = 0

for i in range(3, number+1):
    for j in range(1, i):
        if i % j == 0:
            sum = sum+i
    if sum == number:
        print(j, end=" ")
'''


'''
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i,end=(" "))


adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)
'''
