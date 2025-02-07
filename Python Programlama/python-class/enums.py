from enum import Enum, auto

class AracTuru(Enum):
    OTOMOBIL = auto()
    MOTOSIKLET = auto()
    KAMYON = auto()
    BISIKLET = auto()
    OTOBUS = auto()

# Enum üyelerine erişim
print(AracTuru.OTOMOBIL)
print(AracTuru.MOTOSIKLET.value)

# Otomatik değer atama
print(AracTuru.BISIKLET.value)

# Enum üyelerini liste olarak alma
arac_turleri_listesi = list(AracTuru)
print(arac_turleri_listesi)

# Enum üyelerini döngü ile gezme
for arac in AracTuru:
    print(arac.name, arac.value)