#fungsi open(filename, mode)
f = open('workfile.txt','w')
with open('workfile.txt') as f:
    read_data = f.read()

#objek file yg telah ditutup akan gagal saat akan digunakan kembali
print(f.closed)

f.read()