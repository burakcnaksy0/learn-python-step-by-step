import random

A=[1,2,3,4,5]
B=['t','u','v','w','x','y','z']

num_functions =100000
count_one_to_one=0

for i in range(num_functions):
    function={}

    for element in A:
        choice=random.choice(B)

    while choice in function.values():
        choice = random.choice(B)
        function[element]=choice

if len(set(function.values()))==len(A):
    count_one_to_one +=1

print("Number of one to one functions:",count_one_to_one)

    