# string demo

website = 'http://www.sadikturan.com'
course = 'python kursu : baştan sona python proglama rehberiniz ( 40 saat )'

print(len(course))
print(website[7:10])
print(website[22:len(course)-1])
print(course[0:15])
print(course[len(course)-16:len(course)])
print(course[::])
print(course[::-1])

name,surname,age,job= 'burak','aksoy',21,'mühendis'

result = 'my name is {}{} and I am {} years old . I am a {} '.format(name,surname,age,job)
print(result)

result1 = f'my name is {name}{surname} and I am {age} years old. I am a {job}'
print(result1)
