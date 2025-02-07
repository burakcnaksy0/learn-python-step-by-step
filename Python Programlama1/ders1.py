x = 10
y = "burak"
a = 'c'
b = True

print(x)
print(id(x))
print(y)
print(id(y))
print(a)
print(id(a))
print(b)
print(id(b))

a1, b1, c1 = 1, 2, 3
print(a1, b1, c1)

a2 = b2 = c2 = 45
print(a2, b2, c2)


k, l = 1, 2
print(k, l)
k, l = l, k
print(k, l)
