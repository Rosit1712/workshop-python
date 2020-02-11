#fungsi range()
for i in range(5):
    print(i)
#range() dengan awal dan akhir yang ditentukan
range(5,10)
range(0,10,3)
range(-10,-100,-30)

a = ['Mary','had','a','little','lamb']
for i in range(len(a)):
    print(i,a[i])

#return range
print(range(10))

#sum range
sum(range(4))

#mengambil list dari sebuah range
list(range(4))