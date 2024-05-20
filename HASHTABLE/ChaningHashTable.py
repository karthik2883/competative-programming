<<<<<<< HEAD
class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]

=======
class HashTable:  
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]
        
>>>>>>> 53e422d3ac48e27c1ff90f2963aa19724bb18bdd
    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX
<<<<<<< HEAD

=======
    
>>>>>>> 53e422d3ac48e27c1ff90f2963aa19724bb18bdd
    def __getitem__(self, key):
        arr_index = self.get_hash(key)
        for kv in self.arr[arr_index]:
            if kv[0] == key:
                return kv[1]
<<<<<<< HEAD

=======
        return None
            
>>>>>>> 53e422d3ac48e27c1ff90f2963aa19724bb18bdd
    def __setitem__(self, key, val):
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key, val)
                found = True
        if not found:
            self.arr[h].append((key, val))
<<<<<<< HEAD

=======
        
>>>>>>> 53e422d3ac48e27c1ff90f2963aa19724bb18bdd
    def __delitem__(self, key):
        arr_index = self.get_hash(key)
        for index, kv in enumerate(self.arr[arr_index]):
            if kv[0] == key:
<<<<<<< HEAD
                print("del", index)
=======
>>>>>>> 53e422d3ac48e27c1ff90f2963aa19724bb18bdd
                del self.arr[arr_index][index]
