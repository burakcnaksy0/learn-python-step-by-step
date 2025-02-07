
name = input("entry your name : ")
print("hello",name)

age = input("entry your age : ")
age1=int(age) +10
print("age :",age1)

# kullanıcıdan kısa ve uzun kenar değerlerini alarak dikdörtgenin alan ve çeveresini hesaplayan algoritma

kısa_kenar=int(input("entry a short value :"))
long_value=int(input("entry a long value "))
cevre = 2*(kısa_kenar+long_value)
alan = kısa_kenar*long_value

print("alan : {} and cevre : {}".format(alan,cevre))


number1 =int(input(("entry a value :")))
number2 =int(input(("entry a value :")))
number3 =int(input(("entry a value :")))

sum=number1+number2+number3
multiply = number3*number2*number1
average = sum/3
print("sum is ",sum)
print("multıply is ",multiply)
print("average is ",average)

