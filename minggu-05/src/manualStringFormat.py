#tabel pangkat 2 dan 3 scr manual
for x in range(1, 11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
    print(repr(x*x*x).rjust(4))

#fungsi str.zfill()
print('Fungsi str.zfill()')
print('12'.zfill(5))
print('-3.14'.zfill(7))
print('3.14159265359'.zfill(5))