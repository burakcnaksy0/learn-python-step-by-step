# dictionary

#      (key - value ilişkisi)

# plakalar = {'key' : value}

plakalar = {'kocaeli': 41, 'istanbul': 34}

print(plakalar['kocaeli'])

print(plakalar['istanbul'])

plakalar['ankara'] = 6     # ekleme yaptık..

print(plakalar)


users = {
    'burakAksoy': {
        'roles': ['users'],
        'age': 21,
        'job': 'student',
        'email': 'burak@gmail.com',
        'phone': 43234
    },

    'beratAksoy': {
        'roles': ['admin', 'user'],
        'age': 13,
        'job': 'student',
        'email': 'berat@gmail.com',
        'phone': 434353

    }
}

print(users['burakAksoy'])
print(users['burakAksoy']['age'])
print(users['burakAksoy']['job'])
print(users['burakAksoy']['email'])
print(users['burakAksoy']['phone'])

print(users['beratAksoy']['roles'][0])
