class Queue:
    def ___init___(self):
        self.items = []

    def push(self,item):
        self.items.append(item)

    def empty(self):
        if(len(self.items) == 0):
            return True
        else:
            return False 

    def pop(self):
        if(self.empty()):
            print('Empty Queue')
            return None
        else:
            self.items.pop(0)
            return None
    
    def front(self):
        if(self.empty()):
            return None
        else:
            return self.items[0]





    
    
    

    
        


















