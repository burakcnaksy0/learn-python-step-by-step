import sqlite3

class Room():
    room_list = []

    def __init__(self, no, person_number, avaiable):
        self.no = no
        self.person_number = person_number
        self.avaiable = avaiable
        self.room_list.append(self)

    # avaiable = 0 ise oda dolu  and avaiable = 1 ise oda boş.
    @classmethod
    def show_rooms(cls):
        for room in cls.room_list:
            print("room no : ", room.no)
            print("room person number : ", room.person_number)
            print("room avaiable : ", room.avaiable)
            print("******************************************")


class DatabaseConnection():
    def __init__(self, database_name, table_name):
        self.database = sqlite3.connect(database_name)
        self.cursor = self.database.cursor()
        self.table = table_name
        query = "CREATE TABLE IF NOT EXISTS {} (no INTEGER PRIMARY KEY AUTOINCREMENT,person_number INTEGER NOT NULL,avaiable INTEGER)".format(
            self.table)
        self.cursor.execute(query)
        self.database.commit()  # Tablo oluşturma işlemini kaydet

    def brings_to_room(self):
        query1 = "SELECT * FROM {}".format(self.table)
        self.cursor.execute(query1)
        Room.room_list.clear()
        for room in self.cursor:
            room1 = Room(room[0], room[1], room[2])

    def add_room(self, person_number, avaiable):
        query2 = "INSERT INTO {} (person_number,avaiable) VALUES(?,?)".format(self.table)
        self.cursor.execute(query2, (person_number, avaiable))
        self.database.commit()
        self.brings_to_room()

    def to_fill_room(self, no):
        query3 = "SELECT avaiable FROM {} WHERE no = {}".format(self.table, no)
        self.cursor.execute(query3)
        avaiable = self.cursor.fetchone()
        if avaiable is None:
            print("Room not found.")
            return
        if avaiable[0] == 1:
            query4 = "UPDATE {} SET avaiable = 0 WHERE no = {}".format(self.table, no)
            self.cursor.execute(query4)
            self.database.commit()
            self.brings_to_room()
            print("room reserved")
        else:
            print("room is not available.")

    def to_empty_room(self, no):
        query4 = "SELECT avaiable FROM {} WHERE no = {}".format(self.table, no)
        self.cursor.execute(query4)
        avaiable = self.cursor.fetchone()
        if avaiable is None:
            print("Room not found.")
            return
        if avaiable[0] == 0:
            query5 = "UPDATE {} SET avaiable = 1 WHERE no = {}".format(self.table, no)
            self.cursor.execute(query5)
            self.database.commit()
            self.brings_to_room()
            print("room empty")
        else:
            print("room is already empty.")

    def filter_room(self, person_number):
        query6 = "SELECT * FROM {} WHERE person_number = {} and avaiable = 1".format(self.table, person_number)
        self.cursor.execute(query6)
        results = self.cursor.fetchall()
        if not results:
            print("No available rooms found for {} persons.".format(person_number))
            return
        for room in results:
            print("room no : ", room[0])
            print("room person number : ", room[1])
            print("room avaiable : ", room[2])
            print("******************************************")


database = DatabaseConnection("HotelReservationSystem_Database.sqlite", "Room")
'''
database.add_room(3, 1)   # 3 kişilik
database.add_room(4, 0)   # 4 kişilik
database.add_room(2, 1)   # 2 kişilik
database.add_room(6, 0)   # 6 kişilik
database.add_room(2, 0)   # 2 kişilik
database.add_room(5, 1)   # 5 kişilik
database.add_room(3, 0)   # 3 kişilik
database.add_room(4, 1)   # 4 kişilik
database.add_room(6, 1)   # 6 kişilik
database.add_room(2, 0)   # 2 kişilik 
'''
database.brings_to_room()
database.to_empty_room(3)
Room.show_rooms()
