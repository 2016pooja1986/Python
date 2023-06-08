# concatenate (+) and replicate(*) operator

print(2*'many ' + ' congratulations')

str = "welCoME To TgC animation"
str1= "welcome"
str2="TGC5"

# .capitalize, .upper(),.lower(),.swapcase()

print(str.capitalize())
print(str.upper())
print(str.lower())
print(str.swapcase())

# .islower operator

print(str.islower())
print(str1.islower())

# .isupper operator

print(str.isupper())
print(str2.isupper())

# .isalpha operator

print(str.isalpha())
print(str1.isalpha())
print(str2.isalpha())

# .isalnum operator
print(str1.isalnum())
print(str2.isalnum())
print(str.isalnum())

# len() operator

print("length of string is ",len(str))

# .rstrip(),.lstrip() and strip()

print(str.rstrip('animation'))
print(str.lstrip('welcome'))
print(str.strip('tion'))
print(str.strip('wel'))
print(str.strip('To'))

#.endswith(string,begin,end),.startswith(string,begin,end)

print(str.endswith('ion'))
print(str.endswith('t',3,21))
print(str.startswith('we'))
print(str.startswith('c',2,24))

#.find(string,begin,end),.index(string,begin,end)
print(str.find('o'))
print(str.find('o',6))
print(str.find('c',3,24))

print(str.index('To'))
print(str.index('o',6))
#####print(str.index('c',3,24))

#.count(string,begin,end)
print(str.count('o'))
print(str.count('o',6))
print(str.count('C',3,24))
#.replace()

print(str.replace('TgC', 'TGC'))
print(str1.replace('come', 'COME'))


