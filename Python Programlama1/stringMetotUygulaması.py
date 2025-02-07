# string metot uygulaması

website = ' http://www.sadikturan.com '
course = 'python kursu : baştan sona python proglama rehberiniz ( 40 saat )'

result = ' hello world '.strip()     # istenilen silmeleri yapar
print(result)
result = ' hello world '.lstrip()    # soldaki boşlukları siler
print(result)
result = ' hello world '.rstrip()    # sağdaki boşulları siler
print(result)


result1= 'http://www.sadikturan.com'.strip('htp:/w.com')   # istenilenler silindi...
print(result1)

result2 = course.count('a')    # metin içinde istenen ifadelerin sayısını gösterir.
print(result2)

result3 = ' hello '.isalpha()    # alfabatik olma durumunu inceler.
print(result3)

result4 = course.replace(' ','_')
print(result4)

result5= ' hello world '.replace('world',' there ')
print(result5)

result6 = course.split(' ')    # dizilere ayırma işlemi yapar.
print(result6)
abc = result6[2]
print(abc)