#  liste

sayı = int(input("entry a value : "))
toplam = 0
for i in range(sayı+1):
    if i % 2 == 1:
        toplam = toplam+i

print("tek sayıların toplamı : ", toplam)
