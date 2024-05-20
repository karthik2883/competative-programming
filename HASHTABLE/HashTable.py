# """

<<<<<<< HEAD
"""


=======
# """
>>>>>>> 53e422d3ac48e27c1ff90f2963aa19724bb18bdd
# class HashTable:
#     def __init__(self):
#         self.Max = 100
#         self.Arr = [None] * self.Max
<<<<<<< HEAD
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
=======

#     def get_hash(self,key):
#         sum = 0
#         for c in key:
#             sum += ord(c)
#         return sum % self.Max

#     def __setitem__(self, key, value):
#          h = self.get_hash(key)
#          self.Arr[h] = value

#     def __getitem__(self, key):
#         h = self.get_hash(key)
#         return  self.Arr[h]

#     def __delitem__(self, key):
#         h = self.get_hash(key)
#         self.Arr[h] = None

>>>>>>> 53e422d3ac48e27c1ff90f2963aa19724bb18bdd

# h = HashTable()
# h["march 12"] = 788
# h["march 6"] = 333
# h["march 8"] = 222

# del h["march 8"]
# print(h["march 8"])


class HashTable:

    def __init__(self) -> list:
        self.MAX = 100
        self.Arr = [None] * self.MAX

    def get_hash(self,key):
        s = 0
        for i in key:
            s += ord(i)
        return s % self.MAX    
    
    def __setitem__(self,key,value):
        h = self.get_hash(key)
<<<<<<< HEAD
        return self.Arr[h]
=======
        self.Arr[h] = value
>>>>>>> 53e422d3ac48e27c1ff90f2963aa19724bb18bdd

    def __getitem__(self,key):
        h = self.get_hash(key)
        return self.Arr[h]
    
    def __delitem__(self,key):
        h  = self.get_hash(key)
        self.Arr[h] = None

<<<<<<< HEAD
h = HashTable()
h["march 12"] = 788
h["march 6"] = 333
h["march 8"] = 222
print(h["march 8"])
=======
# h = HashTable()
# h["march 12"] = 788
# h["march 6"] = 333
# h["march 8"] = 222

# del h["march 8"]

# print(h["march 8"])

class Customer:
    def __init__(self) ->None:
         self.customer = HashTable()

    def add_customer(self,name,number):
        self.customer[name] = number
    def get_customer(self , name):
        return self.customer[name]



customer = Customer()
customer.add_customer("Navin", 788)
customer.add_customer("a", 788)
customer.add_customer("b", 788)
customer.add_customer("c", 788)

print(customer.get_customer("c"))
>>>>>>> 53e422d3ac48e27c1ff90f2963aa19724bb18bdd
