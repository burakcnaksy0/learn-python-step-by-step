# ucgen cizme

print(" ")

i = 1
str = '*'
while i < 11:
    print(str*i)
    i += 1

print(" ")

j = 11
while j > 0:
    print(str*j)
    j -= 1

print(" ")

k = 21
while k > 0:
    print(str*k)
    k -= 2


i = 15
for j in range(1, 12, 2):
    for k in range(0, (12-j)//2):
        print(end=" ")
    for j in range(0, j):
        print("x", end="")
    for k in range(0, (12-j)//2):
        print(end=" ")
    print(end="\n")
