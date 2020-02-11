#contoh pembuatan fungsi fibbonaci
def fib(n):
    a,b = 0,1
    while a < n:
        print(a,end=' ')
        a,b = b, a+b
    print()

fib(2000) #panggil fibbonaci

#renaming
fib
f = fib
f (100)

#fungsi dengan print
fib(0)
print(fib(0))

#fibbonaci tanpa print
def fib2(n):
    result = []
    a,b = 0,1
    while a<n:
        result.append(a) #menampilkan
        a, b = b, a+b
    return result

f100 = fib2(100)
print(f100)