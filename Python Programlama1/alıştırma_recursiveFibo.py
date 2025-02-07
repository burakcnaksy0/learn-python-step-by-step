# recursive fibonacci

# kendisi ve kendinden onceki sayı toplamı seklinde gider

# 0 1 1 2 3 5 8 13 21 34 ...

def fibonacci(sayı):

    if sayı == 0 or sayı == 1:
        return sayı
    return fibonacci(sayı-1) + fibonacci(sayı-2)

print(fibonacci(3))
