# 1 den n e kadar olan sayıları yazdırma

n = int(input("entry a value : "))

i=1

while (i<(n+1)):
    print(i)
    i+=1
   
# 1 den n e kadar olan çift sayıları yazdırma

j=1

while (j<(n+1)):
    if j%2==0:
        print(j)
    j += 1


# sonsuz döngü

k=1

while (k<=n):
    print(k)

# 1 den n e kadar sayıalrın toplamı

a=1
sum=0
    
while (a<=n):
    sum+=a
    a+=1

print(sum)


# faktorıyel hesaplama

b=1
value=1

while (b<=n):
    value*=b
    b+=1
print(value)


# iki sayı arasındaki sayıların toplamı

m =int(input("entry a value : "))
sum=0
if n>m:
    m+=1
    while (m<n):
        sum+=m
        m+=1
elif m>n:
    n+=1
    while (m > n):
        sum += n
        n+=1


print(sum)