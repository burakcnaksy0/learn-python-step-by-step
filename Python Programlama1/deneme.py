
a = int(input("ENTRY A VALUE : "))
b = 0
sum = 0

while b < a:
    b += 1
    sum += b
print("SUM İS {}".format(sum))


number = int(input("ENTRY A VALUE : "))
i = 0
top = 0
while i < number:
    i += 1
    if i % 2 == 0:
        top += i
print("YOUR SCORE İS {}".format(top))


text = input("PLEASE ENTRY A TEXT :")
count = 0
for i in text:
    if i == "a" or i == "e" or i == "i" or i == "ı" or i == "u" or i == "ü" or i == "o" or i == "ö":
        count += 1
print("VOWEL NUMBER : {}".format(count))


