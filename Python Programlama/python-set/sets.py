#Python'da Set Nedir?
#Python'da Set Ozellikleri
#1-Benzersiz Elemanlar 2-Sirasiz listeleme 3-Degistirilebilir olmasi

#ornek1 benzersiz eleman
numbers=[1,2,2,3,4,4,5,6,6]
unique_numbers=set(numbers)
print(unique_numbers)

#ornek2 kesisim bulma
set1={1,2,3,4}
set2={3,4,5,6}
common_elements=set1.intersection(set2)
print(common_elements)

#ornek3 set nasil olusturulur
my_set=set()
my_set={1,2,3,4}
print(my_set)

#ornek4 set metotlarinin kullanimi
fruits={"apple","banana","cherry"}
print(fruits)
fruits.add("orange")
print(fruits)

fruits.remove("cherry")
print(fruits)