class Complex:
    def __init__(self, realpart, imag):
        self.r = realpart
        self.i = imag


x = Complex(3.0, -4.5)
print(x.r, x.i)
