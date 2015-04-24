            #Queue class
class Queue(object):
    
    def __init__(self, name):
        self.qlist = []
    
    def insert(self, element):
        self.qlist.append(element)
        
    def remove(self):
        if self.qlist == []:
            raise ValueError()
        else:
            element = self.qlist[0]
            self.qlist.remove(element)
            return element

q = Queue('Paul Johan Seim')
print q