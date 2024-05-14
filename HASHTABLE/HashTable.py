"""

"""


# class HashTable:
#     def __init__(self):
#         self.Max = 100
#         self.Arr = [None] * self.Max
#
#     def get_hash(self,key):
#         sum = 0
#         for c in key:
#             sum += ord(c)
#         return sum % self.Max
#
#     def __setitem__(self, key, value):
#          h = self.get_hash(key)
#          self.Arr[h] = value
#
#     def __getitem__(self, key):
#         h = self.get_hash(key)
#         return  self.Arr[h]
#
#     def __delitem__(self, key):
#         h = self.get_hash(key)
#         self.Arr[h] = None
#
#
# h = HashTable()
# h["march 12"] = 788
# h["march 6"] = 333
# h["march 8"] = 222
#
# #del h["march 8"]
# print(h)


class HashTable:

    def __init__(self):
        self.MAX = 100
        self.Arr = [None] * self.MAX

    def get_hash(self, key):
        sum = 0
        for c in key:
            sum += ord(c)
        return sum % self.MAX

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        self.Arr[h] = value

    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.Arr[h]

    def __delitem__(self, key):
        h = self.get_hash(key)
        self.Arr[h] = None

h = HashTable()
h["march 12"] = 788
h["march 6"] = 333
h["march 8"] = 222
print(h["march 8"])