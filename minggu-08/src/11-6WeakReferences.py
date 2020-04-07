import weakref, gc
class A:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)

a = A(10)                       #create references
d = weakref.WeakValueDictionary()
d['primary'] = a                #does not create reference
print(d['primary'])             #fetch the object if it is still alive
print()
del a                           #remove the one reference
gc.collect()                    #run garbage collection right away
print()
d['primary']                    #entry was automaticaly removed