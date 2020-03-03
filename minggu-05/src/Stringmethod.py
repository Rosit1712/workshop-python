#basic str.format()
print('We are the {} who say "{}!"'.format('knights', 'Ni'))

#penggunaan {} dengan posisi index= 0,1,2... untuk mengganti objek yang dikirm ke str.format()
print('{0} and {1}'.format('spam', 'eggs'))
print('{1} and {0}'.format('spam', 'eggs'))

#menggunakan keyword sbg argument di str.format()
print('This {food} is {adjective}'.format(food='spam', adjective ='absolutely horrible'))

#kombinasi keyword dengan posisi sbg argumen
print('The story of {0}, {1}, and {other}.'.format('Bill','Manfred',other='George'))

#referensi variabel menjadi diformat brdsrkan nama bukan posisi saat string terlalu panjang menggunakan []
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack:{0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; Dcab: {0[Dcab]:d}'.format(table))

#menggunakan notasi **
print('Jack:{Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))

#mengembalikan dictionary yg mengandung semua variabel lokal
#contoh menampilkan nilai integer dgn pangkat 2 dan 3
for x in range (1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))