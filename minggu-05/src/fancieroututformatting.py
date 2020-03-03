#formatted String literals
year = 2016
event = 'Referendum'
print('Formatted String literals')
print(f'Results of the {year} {event}')

#str.format()
yes_votes = 42_572_654
no_votes = 43_132_495
percentage = yes_votes / (yes_votes+no_votes)
print('str.function()')
print('{:9} YES votes {:2.2%}'.format(yes_votes, percentage))

#example
print('Contoh:')
s = 'Hello World'
print(str(s)) #str()
print(repr(s)) #repr()
print(str(1/7))
x = 10 * 3.25
y = 200 * 200
s = 'The value of x is ' + ', and y is ' + repr(y) + '...'
print(s)
hello = 'hello, world\n' #repr() string menambah quotes dan \
hellos = repr(hello)
print(hellos)
print(repr((x, y, ('spam', 'eggs')))) #repr() dapat berupa objek acak python