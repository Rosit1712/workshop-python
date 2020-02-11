#Search prime number 2 to 10
for n in range(2,10):
    for x in range(2,n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
        else:
            #menampilkan bil prima
            print(n,'is a prime number')


#Search even number keyword continue
for num in range(2,10):
    if num % 2 == 0:
        print("Found an even number ",num)
        continue
    
    print("Found a number",num)
