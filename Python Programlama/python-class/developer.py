from ders11 import *

#Inherited or Subclass (note Human in bracket)

class Developer(Human):
    def __init__(self, firstname, lastname, status):
        #self.firstname=firstname
        #self.lastname=lastname
        #self.status=status
        super().__init__(firstname, lastname, status)


developer=Developer(input("firstname:"),input("lastname:"),input("status:"))
developer.display()  