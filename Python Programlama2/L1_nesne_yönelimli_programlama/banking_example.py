class Banka():
    def __init__(self, name, surname, salary):
        self.name = name
        self.surname = surname
        self.salary = salary

    @staticmethod
    def isimSoyIsimKontrol(name):
        pass

    def profilGoruntule(self):
        print("name : ", self.name)
        print("surname : ", self.surname)
        print("salary : ", self.salary)

    def paraYatirma(self, yatıralacakPara):
        self.salary += yatıralacakPara
        self.profilGoruntule()

    def paraGonderme(self, gönderilecekPara):
        self.salary -= gönderilecekPara
        self.profilGoruntule()


b1 = Banka("burak", "aksoy", 1000)
b1.profilGoruntule()
b1.paraGonderme(600)
b1.paraGonderme(600)
b1.paraGonderme(600)
b1.paraYatirma(17001)
