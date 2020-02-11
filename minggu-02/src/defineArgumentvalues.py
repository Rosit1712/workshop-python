def ask_ok(prompt, retries=4,reminder='Please try again'):
    while True:
        ok = input(prompt)
        if ok in ('y','ye','yes'):
            return True
        if ok in ('n','no','nop','nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)
#panggil fungsi
ask_ok('Do you really want to quit?')
#default value 
i =5
def f(arg=i):
    print(arg)
i=6
f()
#pemanggil default dengan nilai digabung
def fb(a,L=[]):
    L.append(a)
    return L
print(fb(1))
print(fb(2))
print(fb(3))

#dibedakan
def fa(a,L=None):
    if L is None:
        L = []
    L.append(a)
    return L
print(fa(1))
print(fa(2))
print(fa(3))