f = open("workfile.txt", "r+")

print(f.read())
#readline() membaca 1 baris teks difle dibaris baru ditandai \n
print(f.readline())

#loop dengan readline()
for line in f:
    print(line, end='')

f.write('This is a test\n')
value = ('the answer', 42)
s = str(value) #mengubah tuple menjadi string
f.write(s)

f = open('workfile.txt', 'rb+')
print(f.write(b'012345678abcdef'))

print(f.seek(5))

print(f.read(1))

print(f.seek(-3, 2))

print(f.read(1))