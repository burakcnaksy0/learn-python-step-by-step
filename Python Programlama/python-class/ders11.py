class Human:
    #constructor yapici method
    def __init__(self,firstname,lastname,status):
        self.firstname=firstname
        self.lastname=lastname
        self.status=status
    
    
    def  display(self):
        print("firstname:",self.firstname)
        print("lastname:",self.lastname)
        print("status:",self.status)    