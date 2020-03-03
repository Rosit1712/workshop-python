#penggunaan f-string (f atau F sebagai ekspresion)
import math
print(f'The Value of pi is approximately {math.pi:.3f}.')
#passing integer
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print(f'{name:10} ==> {phone:10d}')

#modifier sebelum f, '!a' = ascii(), '!s' = str(), '!r' = repr()
animals = 'eels' 
print(f'My hovercraft is full of {animals}.')
print(f'My hovercraft is full of {animals!r}')