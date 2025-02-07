class Car():
    '''
    default public
    --private
    -semi-private
    '''
    carlist = []

    def __init__(self, brand, speedİncrease, speedDecrease):
        self.speed = 0
        self.brand = brand
        self.speedİncrease = speedİncrease
        self.speedDecrease = speedDecrease
        self.carlist.append(brand)

    def showInfo(self):
        print(self.brand)

    def spdİnc(self):
        self.speed += self.speedİncrease
        print(self.speed)

    def spdDec(self):
        self.speed -= self.speedDecrease
        print(self.speed)

    @classmethod
    def showCars(cls):
        for car in cls.carlist:
            print(car)

    @staticmethod
    def reverseShow(string):
        print(string[::-1])


car1 = Car("BMW", 50, 30)
car2 = Car("mercedes", 100, 35)

car1.showInfo()
car2.showInfo()

car1.spdİnc()
car2.spdİnc()

car1.spdDec()
car2.spdDec()

Car.showCars()
Car.reverseShow(car2.brand)