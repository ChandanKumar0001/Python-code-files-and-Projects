# Arithmatic Operators
a = 12
b = 4

print(a+b)
print(a-b)
print(a*b)
print(a/b)  # this devision symbol / always gives us float value
print (a%b)  # this % modulo operator always gives remainder
print (a**b)  # this ** power operator always teat as a^b (a par power b)


print("-----------------------------------------------------------------------------------------------")

# Realtional/Comparison Operators  -> it always gives boolean value as output (True/False)
x = 50
y = 20

print(x == y)
print(x != y)
print(x >= y)
print(x <= y)
print(x > y)
print(x < y)


print("-----------------------------------------------------------------------------------------------")

# Assignment Operators

num = 10
#num += 5  # or num = num + 5
# num -= 5
# num *= 10
# num /= 5
# num %= 5
num **= 5
print("num :", num)

print("-----------------------------------------------------------------------------------------------")

# Logical Operators

a1 = 50
b1 = 30

print(not False)
print(not (a > b)) # not means it gives opposite of origional output value

print("---------------------------")

val1 = True
val2 = False

print("AND operator :", val1 and val2)  # if both value is True then output is True else it gives False 

print("OR operator :", val1 or val2)  # if minimum one value is True then output is True if both is False then the output is False 
print("OR operator :", (a1 == b1) or (a1 >b1 )) 