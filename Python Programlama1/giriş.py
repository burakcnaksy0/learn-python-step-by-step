name = 'burak'
surname = 'aksoy'
age = 21
space= ' '

greetings = 'my name is '+name + ' '+surname+' and \nI am '+str(age)+' years old'
print(greetings)
print(len(greetings))                 # karakter sayısını verir.
print(greetings[0])                   # indexteki karakteri verir.
print(greetings[len(greetings)-1])    # son karakteri verir.
print(greetings[0:22])                # indeksler arasındaki karakterleri verir.
print(greetings[0:20:2])              # indeksler arasını ikişer ikişer alır.


print(f'my name is {name}{space}{surname} and I am {age} years old.')