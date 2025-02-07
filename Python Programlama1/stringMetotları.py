# string metotları

message = ' Hello there . My name is burak aksoy'
message1 = ' Hello there . My name is burak aksoy'
message2 = ' Hello there . My name is burak aksoy'
message3 = ' Hello there . My name is burak aksoy'
message4 = ' Hello there . My name is burak aksoy'
message5 = ' Hello there . My name is burak aksoy'
message6 = ' Hello there . My name is burak aksoy'
message7 = ' Hello there . My name is burak aksoy'



message = message.upper()    # bütün harfler büyük
print('1 : '+message)
message1 = message1.lower()    # bütün harfler küçük
print('2: '+message1)
message2 = message2.title()    # kelimelerin başındaki harfler büyük
print('3 : '+message2)
message3 = message3.strip()    # metindeki boşlukları siler.
print('4 : '+message3)
message4 = message4.split()    # metini her boşluktan sonra ayırır. // parçalar
print(message4)
message5 = message5.replace('burak','berat')   # değiştirme işlemi yapar.
print('6 : '+message5)
index = message6.find('burak')      # bulundugu indeks sayısını verir.
print(index)
message = message7.center(100,'*')
print('8 : '+message)