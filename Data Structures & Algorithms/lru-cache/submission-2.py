class LRUCache:

    def __init__(self, capacity: int):
        self.dicto = OrderedDict()
        self.cap = capacity
        

    def get(self, key: int) -> int:
        if key in self.dicto:
            self.dicto.move_to_end(key)
            return self.dicto[key]
        return -1
        
        
    def put(self, key: int, value: int) -> None:
        if key in self.dicto:
            self.dicto.move_to_end(key)
            self.dicto[key] = value
        else:
            if len(self.dicto) >= self.cap:
                self.dicto.popitem(last=False)
                self.dicto[key] = value
            else:
                self.dicto[key] = value
                


        
        
