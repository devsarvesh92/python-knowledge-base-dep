class HashTable:
    """
    Defines hash table
    """

    def __init__(self):
        self.MAX = 100
        self.arr = [[] for _ in range(self.MAX)]

    def get_hash(self,key):
        """
        Get hash of the key
        """

        hash = 0
        for char in key:
            hash+=ord(char)
        
        return hash % self.MAX
    
    def __getitem__(self,key):
        hv = self.get_hash(key)

        for el in self.arr[hv]:
            if el[0] == key:
                return el[1]

    
    def __setitem__(self,key,value):
        hv = self.get_hash(key=key)
        
        found=False
        for id,el in enumerate(self.arr[hv]):
            if el[0] == key:
                found=True
                self.arr[hv][id] = (key,value)
        if not found:
            self.arr[hv].append((key,value))

    def __delitem__(self,key):
        hv=  self.get_hash(key=key)

        for id,el in enumerate(self.arr[hv]):
            if el[0] == key:
                del self.arr[hv][id]


    def __str__(self):
        val = ""
        for items in self.arr:
            for item in items:
                val +=item[1]

        return val
            


d = HashTable()
d['name']='sarvesh'
d['age']='20'
print(d['age'])