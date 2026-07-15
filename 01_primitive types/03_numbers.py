##

import math

x = 1
y = 1.1
z = 1 + 2j

print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3)  # float division
print(10 // 3)  # floor division
print(10 % 3)  # modulus
print(10 ** 3)  # exponentiation

x = 10
x += 3  # x = x + 3
print(x)  # 13

# functions to work with number
print(round(2.9))  # 3
print(abs(-2.9))  # 2.9

# if we want to use more math functions, we can use the math module

print(math.ceil(2.9))  # 3

# more math functions: https://docs.python.org/3/library/math.html

# type conversion
x = input("x: ")  # user input is always a string
print(type(x))  # <class 'str'>
# python can not add string and integer, so we need to convert the string to integer
y = int(x) + 1

int(x)
float(x)
bool(x)  # if x is 0, then it will return False, otherwise True
str(x)  # convert to string

print(f"x: {x}, y: {y}")  # f-string
