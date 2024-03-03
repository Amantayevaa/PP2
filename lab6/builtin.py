#1_1
def m(n):
    x = 1
    for i in n:
        x*=i
    return x
print(m((4, 5 , 6)))
#2_2
def multiply(a, lst):
    return [a * i for i in lst]

a = 5
List = [1, 2, 3, 4]
b = multiply(a, List)
print(b)

#2
def s(a):
    upperCase = 0
    lowerCase = 0
    for i in a:
        if i.isupper():
            upperCase += 1

        elif i.islower():
            lowerCase+=1
        else:
            pass
    print(f"upper case letters: {upperCase}")
    print(f"lower case letters: {lowerCase}")

s(input("Enter the word: "))

#3
def isPalindrom(str):
    if str == str[::-1]:
        return True
    return False
print(isPalindrom(input()))

#4
import time 
import math
a = int(input("Sample input:\n"))
t = int(input())
time.sleep(t/1000)
sqrt = math.sqrt(a)
print(f"Square root of {a} after {t} miliseconds is {sqrt}")

#5
Tuple = ("ALmaty", "Assemgul", 5, 78)
print(all(Tuple))