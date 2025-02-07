import threading
import time
def print_numbers():
    for i in range(10):
        print(i)


def print_letters():
    for letter in 'abcdefghij':
        print(letter)


#multi threading (Coklu is parcacigi) olusturalim
thread1=threading.Thread(target=print_numbers)
thread2=threading.Thread(target=print_letters)

#multi threading (Coklu is parcacigi) baslatalim
thread1.start()
time.sleep(0.5)
thread2.start()


#main thread (Ana is parcaciginin)
#multi threading (Coklu is parcaciklarinin) bitmesini beklemesi
thread1.join()
thread2.join()
time.sleep(0.5)
print("completed successfully !")              