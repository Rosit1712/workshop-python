class Dog:
    kind = 'canine' #kind yg diakses disemua instance
    def __init__(self, name):
        self.name = name
    

d = Dog('Fido')
e = Dog('Buddy')

print(d.kind) #shared by all dogs
print(e.kind)
print(d.name) #unik name
print(e.name)
