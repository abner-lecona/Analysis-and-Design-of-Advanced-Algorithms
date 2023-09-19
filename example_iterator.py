from ordered_set import OrderedSet

x = [ 3, 7, 10, 20] 
# Using iterators

try:
    it = iter(x)
    print(f'{x = }, {it = }')
    print(f'{next(it) = }')
    print(f'{next(it) = }')
    print(f'{next(it) = }')
    print(f'{next(it) = }')
    print(f'{next(it) = }')
except StopIteration:
    print('stop')

print()

try: 
    it = iter(x)
    print(it)
    while True:
        print(f'{next(it) = }')
except StopIteration:
    print('stop')

print()

for elem in x:
    print(f'{elem = }')
else: 
    print('stop')

s = OrderedSet(['one', 'two', 'three', 'four', 'five'])
it2 = iter(s)
print(f'{next(it2) = }')
print(f'{next(it2) = }')

print()

for str_elem in s:
    print(f'{str_elem = }')