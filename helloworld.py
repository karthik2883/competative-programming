"""print("karthik")
print("age is 40")
a = 10
c = -2.1
print(a+c)
print(a//c , a/c)
color = input("please enter color")

if(color =='red'):
   print("red")
elif(color=='green'):
    print("green")
elif(color=='blue'):
   print("blue")
else:
    print("color",color)

a = int(input("enter first number"))
b = int(input("enter second number"))
c = int(input("enter third number"))
d = int(input("enter fourth number"))

if( a >= b and a >= c and a >= d):
    print("largest number is a:",a)
elif(b >= c and b >= d ):
    print("largest number is b:",b)
elif(c >= d):
     print("largest number is c:", c)
else:
    print("largest number is d:",d)

list = [12,2,4,4,56,565,75,90]
list.append(544)
list.insert(2,27)
list.sort(reverse=True)
print(list)
mv1 = input("Enter 1st movie")
mv2 = input("Enter 2st movie")
mv3 = input("Enter 3st movie")
list = []
list.append(mv1)
list.append(mv2)
list.append(mv3)

print(list)


listPal = [1,2,2,1]
listPalComp = listPal.copy()
listPalComp.reverse()
if(listPal == listPalComp):
   print("Palandrome")
else:
    print("not Palandrome")

mytuple = (1, 2, 3)
print(mytuple.count(2))

dict ={
    "name":"karthik",
    "age":42,
    "subject":["history","Math","DSA"],
    "add":"defence 5/54/2"

}
print(type(dict))
print(dict["subject"][0])
print(dict["add"])

def show(n):
    if(n==0):
        return
    print(n)
    return show(n-1)

show(5)

def sum_list(n):
    if(n == 1 or n == 0):
        return 1
    return  sum_list(n-1)+n

print(sum_list(3))


def listing(allList,idx=0):

    if(idx==len(allList)):
        return

    return listing(allList,idx+1)
num =[1,2,3]
listing(num,0)
# 5!=1*2*3*4*5
def cal_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)
cal_fact(5)

def converTor(usd):
    ind = 83
    return  usd*ind
print(converTor(7000))

def itemRec(n):
    if(n == 0 or n == 1):
        return 1
    return itemRec(n - 1) + n

print(itemRec(5))

#print all element in the list
def print_all_ele(li,idx=0):
    if(len(li) == 0 or idx == -1):
        return
    print(li[idx])
    return print_all_ele(li,idx-1)


list = ["mango","blue berry","gauva"]
print_all_ele(list,len(list) -1)
"""
# OOPS class attributes & instance attributes
#class.attr
#obj.attr
"""
Abstraction:- Hiding the implementation details of the class and only showing the essential features to the user 
Encapsulation:- Wrapping data and function  into single unit(object)
inheritance :-
polymorphism :-
"""



# class Student:
#     # def __init__(self):
#     #     pass
#     college ="Abbc College"
#     name ="Anonymous"
#     def __init__(self, name, mark):
#         self.name = name #obj.attr >class.attr
#         self.mark = mark
#
#     def hello(self):
#         print("welcome student",self.name)
#
#     def get_marks(self):
#          return self.mark
#
# s1 = Student("karthik",89)
# print(s1.name)
# print(s1.mark)
# s1.hello()
# print(s1.get_marks())
#
# s2 = Student("sandhya",89)
# print(s2.name)
# print(s2.mark)
# print(Student.college)
# print(Student.name)
# class Car:
#     color ="blue"
#     brand ="Toyoto"
#
# car1 = Car()
# print(car1.color)
# print(car1.brand)

# class Students:
#
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks
#     @staticmethod
#     def decorator():
#         print("decorator static method")
#     def get_avg(self):
#         sum = self.marks
#         t = 0
#         for a in sum:
#             t += a
#         print("hi",self.name,"Your avg score is", t/3)
#
#
# s1 = Students("karthik",[324,56,45])
# s1.get_avg()

"""
Create Account class with 2 attributes - balance & account nno.
Create Methods for debit, Credit & printing the balance



class Bank:
    def __init__(self, balance, account):
        self.balance = balance
        self.account = account
    def debit(self,amount=0):
        self.balance -= amount
    def credit(self, amount=0):
          self.balance +=  amount
    def printing(self):
        print("Hello Your acc", self.account ,"having this balance : ", self.balance)

bk = Bank(10,1001)
bk.printing()
bk.credit(50)
bk.printing()
bk.debit(5)
bk.printing()


class Car:
    @staticmethod
    def start():
        print("car started")
    @staticmethod
    def stop():
        print("car stoped")

class Toyota(Car):
    def __init__(self, brand):
        self.brand = brand
        print("Your Brand ", self.brand)
    def __color(self,color):
        self.color = color
        print("Alloted color",self.color)
    def allot(self,allot_color):
        self.__color(allot_color)

class Fortuner(Toyota):
    def __init__(self,type):
        self.type = type
        print("Your Brand Type", self.type)

car1 = Fortuner("A")
car1.allot("blue")



class Marks:
    def __init__(self,math,phy,che):
        self.math = math
        self.phy = phy
        self.che = che

    @property
    def percentage(self):
      return str((self.math + self.phy + self.che) /3)+"%"


m1 = Marks(45,12,52)
print(m1.percentage)
m1.phy = 55
print(m1.percentage)


@getter @setter

operator overloading and dunder method
complex number
real number 

"""