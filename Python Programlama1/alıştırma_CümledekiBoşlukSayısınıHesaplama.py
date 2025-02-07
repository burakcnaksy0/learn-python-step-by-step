# cümledeki boşluk sayısını bulma

str1 = "Vikipedi, kullanıcıları tarafından ortaklaşa olarak birçok dilde hazırlanan; özgür, bağımsız, ücretsiz, reklamsız ve kâr amacı gütmeyen bir internet ansiklopedisidir."

counter = 0

for i in str1:
    if i == ' ':
        counter += 1

print("toplam {} tane boşluk vardır".format(counter))

print("sasasa")