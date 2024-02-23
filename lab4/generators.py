#1
def square(n):
    for i in range(n):
        yield i**2

for i in square(5):
    print (i)

#2
def even(n):
    for i in range(n+1):
        if (i%2==0):
            yield str(i)

def main():
    n = int(input("Number: "))
    number = even(n)
    return(','.join(number))

print(main())
#3
def divisible(n):
    for i in range(0, n):
        if (i%3==0 and i%4==0):
            yield i

for i in divisible(int(input())):
    print(i)

#4
def squares(a, b):
    for i in range(a, b+1):
        yield i*i

for i in squares(int(input("a: ")), int(input("b: "))):
    print(i)

#5
def numbers(n):
    for i in range(n, -1, -1):
        yield i
        
for i in numbers(int(input())):
    print(i)