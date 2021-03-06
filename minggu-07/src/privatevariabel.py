class Mapping:
    def __init__(self, iterable):
        self.item_list = []
    
    def update(self, iterable):
        for item in iterable:
            self.item_list.append(item)
        
    __update  = update #private copy of original update() methode

class MappingSubClass(Mapping):

    def udpate(self, keys, values):
        #provides new signature for update()
        #but does not break __init__()
        for item in zip(keys, values):
            self.item_list.append(item)