#1
class String():
    def __init__(self):
        self.Str= ""

    def getString(self):
        self.Str=input()
        
    def printString(self):
        print(self.Str.upper())

Str = String()
Str.getString()
Str.printString()

#2
class Shape():
    def __init__(self):
        pass
    def area(self):
        return 0
    
class Square(Shape):
    def __init__(self, length):
        Shape.__init__(self)
        self.length = length
    
    def area(self):
        return self.length*self.length
    
x = int(input())    
square = Square(x)
print (square.area())

#3
class Shape():
    def __init__(self):
        pass
    def area(self):
        return 0
    
class Rectangle(Shape):
    def __init__(self, length, width):
        Shape.__init__(self)
        self.length = length
        self.width = width
    def area(self):
        return self.length*self.width
    
x = int (input())
y = int (input())
rectangle = Rectangle(x, y)
print(rectangle.area())

#4
import math
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show(self):
        return self.x, self.y
    
    def move(self, x1, y1):
        self.x = self.x+x1
        self.y = self.y+y1
        return self.x, self.y
    def dist(self, point):
        return math.sqrt((point.x - self.x) ** 2 + (point.y - self.y) ** 2)


a = int(input())
b = int(input())
c = int(input())
d = int(input())
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
point1 = Point(a,b)
point2 = Point(c,d)

print(point1.show())
print(point2.show())
print(point1.move(x1,y1))
print(point2.move(x2,y2))
print(point1.dist(point2))

#5
class Account():
    def __init__(self,balance=0):
        self.balance = balance
    def deposit(self):
        money = int(input())
        self.balance = self.balance + money
        return (f"Money in the account ", self.balance, f"Deposited: ", money)
    def withdraw(self):
        money = int(input())
        if self.balance >= money:
            self.balance -= money
            return(f"Money remaining in the account ", self.balance, f"Withdraw: ", money)
        else: 
            return(f"Insufficient")
x = int(input())         
A = Account(x)
print (A.deposit())
print (A.withdraw())

#6
import math
class FilterPrime():
    def isPrime(n):
        if (n==0 or n==1): 
            return False
        for i in range (2, int(math.sqrt(n))+1 ):
            if n % i == 0: 
                return False
        return True
    def filter(numbers):
        return list(filter(lambda x: FilterPrime.isPrime(x), numbers))
x = int(input())
numbers = []
for i in range(x):
    a = int(input("Enter number {}: ".format(i + 1)))  
    numbers.append(a)

A = FilterPrime.filter(numbers)
print(A)



