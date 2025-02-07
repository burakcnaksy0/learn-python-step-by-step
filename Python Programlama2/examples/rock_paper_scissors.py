import random

while True:
    data_list = ["taş", "kağıt", "makas"]
    random_data = random.choice(data_list)

    user_data = input("Please entry a data : ")

    if user_data not in data_list:
        print("yanlış ifade girildi")
    else:
        if random_data == user_data:
            print("berabere")
        elif random_data == "taş" and user_data == "kağıt":
            print("kazandın")
        elif random_data == "taş" and user_data == "makas":
            print("kaybettin")
        elif random_data == "makas" and user_data == "taş":
            print("kazandın")
        elif random_data == "makas" and user_data == "kağıt":
            print("kaybettin")
        elif random_data == "kağıt" and user_data == "makas":
            print("kazandın")
        elif random_data == "kağıt" and user_data == "taş":
            print("kaybettin")
