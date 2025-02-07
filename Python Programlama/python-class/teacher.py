from ders11 import *

# Inherited or Subclass (Note Human in bracket)

class Teacher(Human):
    def __init__(self, firstName, lastName, status):
        # self.firstName=firstName
        # self.lastName=lastName
        # self.status=status
        super().__init__(firstName,lastName,status)
               

teacher=Teacher(input("firstName:"),input("lastName:"),input("status:"))    
teacher.display()       