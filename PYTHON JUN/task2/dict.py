d = {'a': 1, 'b':2, 'c': 3}

d_2 = dict(a=1,b=2, c=3)
print(d_2)

d_2 = dict.fromkeys(['a','b', 'c'],3)
print(d_2)

new_dict = {
    'name': 'userName',
    'info': {
        'age': 0,
    }
    }

print(d['a'])
print(d['b'])

print(d)
d['d'] = 4
print(d)

# print(d['eee'])

print(new_dict['info']['age'])

my_d = dict.fromkeys(['a', 'b', 'c'], 0)

my_d2 = my_d.copy()

my_d.clear()

print(my_d2.items())
print(my_d2.keys())
.not
