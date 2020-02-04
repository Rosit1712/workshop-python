Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> the_world_is_flat = True
>>> if the_world_is_flat:
	print("Be careful not to fall off!")

Be careful not to fall off!
>>> 2+2
4
>>> 50 - 5*6
20
>>> (50 - 5*6)/4
5.0
>>> 8/5
1.6
>>> 17/3
5.666666666666667
>>> 17//3
5
>>> 17%3
2
>>> 5*3+2
17
>>> 5 ** 2 #** = pangkat
25
>>> 2 ** 7
128
>>> width =20
>>> height = 5*9
>>> width*height
900
>>> n #variabel tdk dideklarasikan
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    n #variabel tdk dideklarasikan
NameError: name 'n' is not defined
>>> print("ocnvert integer ke float")
ocnvert integer ke float
>>> 4*3.75-1
14.0
>>> print ("desk calculator")
desk calculator
>>> tac = 12.5 /100
>>> price = 100.50
>>> price * tax
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    price * tax
NameError: name 'tax' is not defined
>>> tax = 12.5 / 100
>>> price = 100.50
>>> price * tax
12.5625
>>> price + _
113.0625
>>> round(_, 2)
113.06
>>> print ("String")
String
>>> 'spam eggs'
'spam eggs'
>>> 'spam eggs' #single quotes
'spam eggs'
>>> 'doesn\'t' #\ untuk memakai ' single quotes
"doesn't"
>>> "doesn't" #penggunakan double quotes
"doesn't"
>>> '"Yes, " they said.'
'"Yes, " they said.'
>>> "\Yes,\" they said."
'\\Yes," they said.'
>>> "\"Yes,\" they said."
'"Yes," they said.'
>>> '"Isn\'t," they said.'
'"Isn\'t," they said.'
>>> '"Isn\'t," they said.'
'"Isn\'t," they said.'
>>> print('"Isn\'t," they said.')
"Isn't," they said.
>>> s = 'First line.\nSecond line.' #\n baris baru
>>> s # tanpa print() akan menampilkan isi variabel s tanpa enter
'First line.\nSecond line.'
>>> print (s)
First line.
Second line.
>>> print('C:\some\name')
C:\some
ame
>>> print(r'C:\some\name')
C:\some\name
>>> #3 time 'un',diikuti 'ium'
>>> 3 * 'un' + 'ium'
'unununium'
>>> 'Py' + 'thon' # 2 string
'Python'
>>> 'membagi string yang terlalu panjang'
'membagi string yang terlalu panjang'
>>> text = ('Put several string within parentheses'
	'to have the joined together.')
>>> text
'Put several string within parenthesesto have the joined together.'
>>> prefix ='Py'
>>> prefix 'thon' #tidak bisa digabung
SyntaxError: invalid syntax
>>> ('un' * 3) + 'ium'
'unununium'
>>> prefix + 'thon'
'Python'
>>> word = 'Python'
>>> word[0]
'P'
>>> word[5]
'n'
>>> word[-1] #karakter terakhir
'n'
>>> word[-3]
'h'
>>> word[-6]
'P'
>>> word[0:2} #karakter dari posisi 0 ke 2
SyntaxError: invalid syntax
>>> word[0:2] #karakter dari 0 ke 2
'Py'
>>> word[2:5] #karakter dari 2 ke 5
'tho'
>>> word[:2] + word[2:]
'Python'
>>> word[:2]
'Py'
>>> word[:4]
'Pyth'
>>> word[42]
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    word[42]
IndexError: string index out of range
>>> word[42:]
''
>>> word[0]='J'
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    word[0]='J'
TypeError: 'str' object does not support item assignment
>>> word[2:] ='py'
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    word[2:] ='py'
TypeError: 'str' object does not support item assignment
>>> 'J' +word[1:]
'Jython'
>>> word[:2]+'py'
'Pypy'
>>> s = 'supercalifraglistiexpialidocious'
>>> les(s)
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    les(s)
NameError: name 'les' is not defined
>>> len(s)
32
>>> squares = [1,4,9,16,25]
>>> squares
[1, 4, 9, 16, 25]
>>> squares[0]
1
>>> squares[-1]
25
>>> squares[:]
[1, 4, 9, 16, 25]
>>> squares + [36, 49, 64, 81, 100]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
>>> cubes = [1, 8, 27, 65, 125]
>>> cubes[3] = 64
>>> cubes
[1, 8, 27, 64, 125]
>>> cubes.append(216)
>>> cubes.append(7**3)
>>> cubes
[1, 8, 27, 64, 125, 216, 343]
>>> letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
>>> letters
['a', 'b', 'c', 'd', 'e', 'f', 'g']
>>> letters[2:5] = ['C', 'D', 'E']
>>> letters
['a', 'b', 'C', 'D', 'E', 'f', 'g']
>>> letters[2:5] = []
>>> letters
['a', 'b', 'f', 'g']
>>> letters[:] = []
>>> letters
[]
>>> letters = ['a', 'b', 'c', 'd']
>>> len(letters)
4
>>> 'fibonacci'
'fibonacci'
>>> a,b = 0,1
>>> while a < 10:
	print(a)
	a,b = b, a+b

0
1
1
2
3
5
8
>>> 
