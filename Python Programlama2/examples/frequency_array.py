array = []
array_len = int(input("entry a array size : "))
for k in range(array_len):
    value = input("entry a value :")
    array.append(value)

checked = []

for i in array:
    if i not in checked:
        count = 0
        for j in array:
            if i == j:
                count += 1
        print(i, "değerinden", count, "tane vardır")
        checked.append(i)
