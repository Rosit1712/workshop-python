class Complex:
    def __init__(self, realpart, imag):
        self.r = realpart
        self.i = imag


x = Complex(3.0, -4.5)
x.counter = 1
while x.counter < 10:
    x.counter = x.counter * 2
print(x.counter)
del x.counter