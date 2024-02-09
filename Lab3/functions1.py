#1
def Ounces(grams):
    ounces = float
    ounces = 28.3495231 * grams
    print(ounces)
Ounces(int(input()))


#2
def temperature(F):
    C = int
    C = (5 / 9) * (F - 32)
    print (C)
temperature(int(input()))

#3
def solve(numlegs, numheads):
    rabbit = (numlegs - 2*numheads)/2
    chicken = numheads - rabbit
    print(int(chicken))
    print(int(rabbit))
solve(94, 35)

#4
def isPrime(n):
    if n<2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
    return True
def filter(numbers):
    prime_numbers = []
    for n in numbers:
        if isPrime(n):
            prime_numbers.append(n)
    return prime_numbers
numbers = [1, 2, 5, 8, 17, 13]
filtered = filter(numbers)
print(filtered)

#5
from itertools import permutations
def print_permutations(str):
    perms = permutations(str)
    for perm in list(perms):
        print(''.join(perm))
str1 = input()
print_permutations(str1)

#6
def reverse(str):
    a = string.split()[::-1]
    b = []
    for i in a:
        b.append(i)
    print(' '.join(b))
string = input()
reverse(string)

#7
def has_33(num):
    for i in range(1, len(num)):
        if num[i-1] == 3 and num[i] ==3:
            return True
    return False
num = [1, 3, 3]
print(has_33(num))
num = [3,3,3]
print(has_33(num))

#8
def spy_game(nums):
    for i in range(2, len(nums)):
        if nums[i-2] == 0 and nums[i-1] == 0 and nums[i] == 7:
            return True
    return False
nums = [1,0,2,4,0,5,7]
print(spy_game(nums))
    
#9
r = int(input())
def volume(r):
    a = pow(r, 3)
    V = (4/3) * 3.14 *a
    print(V)
volume(r) 

#10
def unique(list):
    uniqueList = []
    for i in list:
        if i not in uniqueList:
            uniqueList.append(i)
    return uniqueList
list = [1,1,1,1,4,1,1,5,7,8,6]
print(unique(list))

#11
def isPalindrom(str):
    if str == str[::-1]:
        return True
    return False
print(isPalindrom(input()))

#12
def histogram(list):
    for i in list:
        print ('*' *i )
    
histogram([1,4,8])

#13
import random

def Guess_the_number():
    print("Hello! What is your name?")
    name = input()
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")

    number = random.randint(0,20)
    try_count = 0

    while True:
        print("Take a guess")
        num = int(input())
        try_count += 1

        if (num > number):
            print("Your guess is too high.")
        elif(num < number):
            print("Your guess is too low.")
        else:
            print(f"Good job, {name}! You guessed my number in {try_count} guesses!")
            break
Guess_the_number()


