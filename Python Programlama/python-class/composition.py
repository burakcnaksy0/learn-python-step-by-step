#composition
class ContactInformation:
    def __init__(self, email, phone):
        self.email = email
        self.phone = phone

    def __str__(self):
        return f"Email: {self.email}\nPhone: {self.phone}"

class Employee:
    def __init__(self, employee_id, name, position):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.contact_info = None

    def set_contact_info(self, contact_info: ContactInformation):
        self.contact_info = contact_info

    def __str__(self):
        return f"Employee ID: {self.employee_id}\nName: {self.name}\nPosition: {self.position}\nContact Information:\n{self.contact_info}"

# Örnek Kullanım
employee1 = Employee(1, "Ahmet", "Developer")
contact_info1 = ContactInformation("ahmet@example.com", "555-1234")
employee1.set_contact_info(contact_info1)

employee2 = Employee(2, "Ayşe", "Manager")
contact_info2 = ContactInformation("ayse@example.com", "555-5678")
employee2.set_contact_info(contact_info2)

# Çalışan bilgilerini yazdırma
print(employee1)
print("\n")
print(employee2)