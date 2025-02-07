# listeler

arabalar = ['BMW', 'mercedes', 'opel', 'mazda']

result = len(arabalar)
print(result)

print(arabalar[0])
print(arabalar[len(arabalar)-1])


isCar = 'mercedes' in arabalar    # kümede olma durumuna bakar.
print(isCar)

result1 = arabalar[0:3]     # cutting işlemi yapar.
print(result1)


arabalar[-2:] = ['toyata', 'audi']     # son iki elemanı değiştirdik.
print(arabalar)

result2 = arabalar[::-1]    # diziyi tersten yazdık.
print(result2)

del arabalar[len(arabalar)-1]     # son indeksi sildik
print(arabalar)


studentA = ['burak', 'aksoy', '21', [70, 60, 80]]

sonuc = f'benim adım {studentA[0]}{studentA[1]} ve ben {studentA[2] } yaşındayım , notlarımın ortalaması {(studentA[3][0]+studentA[3][1]+studentA[3][2])/3}'
print(sonuc)


""" 
oluyo ya işte aq 

"""
