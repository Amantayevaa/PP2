from functions1 import Ounces, temperature, solve, filter, print_permutations, reverse, has_33, spy_game, volume, unique, isPalindrom, histogram, Guess_the_number
# 1. Ounces
Ounces(int(input()))

# 2. temperature
F = int(input())
temperature(F)

#3
solve(94, 35)

# 4. filter
numbers = [1, 2, 5, 8, 17, 13]
filtered = filter(numbers)
print(filtered)

# 5. print_permutations
str1 = input()
print_permutations(str1)

# 6. reverse
string = input()
reverse(string)

# 7. has_33
num1 = [1, 3, 3]
print(has_33(num1))
num2 = [3, 3, 3]
print(has_33(num2))

# 8. spy_game
nums = [1, 0, 2, 4, 0, 5, 7]
print(spy_game(nums))

# 9. volume
r = int(input())
volume(r)

# 10. unique
lst = [1, 1, 1, 1, 4, 1, 1, 5, 7, 8, 6]
print(unique(lst))

# 11. isPalindrome
s = input()
print(isPalindrom(s))

# 12. histogram
histogram([1, 4, 8])

# 13. Guess_the_number
Guess_the_number()
