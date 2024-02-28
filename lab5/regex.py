#1
import re
def string_match(s):
    pattern = r'ab*'
    if re.fullmatch(pattern, s):
        return True
    else:
        return False
    
s = input()
if string_match(s):
    print ("String matches the pattern.")
else:
    print("String does not match the pattern.")


#2
import re
def string_match(s):
    pattern = r'ab{2,3}'
    if re.fullmatch(pattern, s):
        return True
    else:
        return False
    
s = input()
if string_match(s):
    print ("String matches the pattern.")
else:
    print("String does not match the pattern.")


#3
import re
def lowercase(text):
        patterns = '^[a-z]+_[a-z]+$'
        if re.findall(patterns, text):
                return("String matches the pattern.")
        else:
                return("String does not match the pattern.")

s=input()
print (lowercase(s))


#4

import re
def uppercase(text):
        patterns = '^[A-Z][a-z]+'
        if re.findall(patterns, text):
                return("String matches the pattern.")
        else:
                return("String does not match the pattern.")

s=input()
print (uppercase(s))


#5
import re
def string_match(s):
    pattern = r'a.*?b$'
    if re.fullmatch(pattern, s):
        return True
    else:
        return False
    
s = input()
if string_match(s):
    print ("String matches the pattern.")
else:
    print("String does not match the pattern.")


#6
import re
def a(s):
    pattern = r"[ ,.]"
    b = re.sub(pattern, ":", s)
    return b
s = input()
replace = a(s)
print(replace)


#7
def camel(s):
    elements = s.split('_')
    c = ''.join(x.capitalize() for x in elements[0:])
    return c


s = input()
c = camel(s)
print(c)

#8
import re
def split_uppercase(s):
    pattern = r"[A-Z][^A-Z]*"
    element = re.findall(pattern, s)
    return element
s = input()
result = split_uppercase(s)
print (result)

#9
import re
def a(s):
    pattern = r"(\w)([A-Z])"
    return re.sub(pattern,r"\1 \2", s)
s = input()
result = a(s)
print(result)


#10
import re
def a(s):
    pattern = r'(?<!^)(?=[A-Z])'
    b = re.sub(pattern, '_', s).lower()
    return b
s = input()
result = a(s)
print(result)
