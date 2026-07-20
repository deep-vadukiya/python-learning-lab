#

# comparison operators
print(10 > 5)  # True
print("bag" > "apple")  # True


# conditional statements
temperature = 35
if temperature > 30:
    print("It's a hot day")
    print("Drink plenty of water")
elif temperature > 20:
    print("It's a nice day")
else:
    print("It's a cold day")

# ternary operator
age = 22
if age >= 18:
    message = 'Eligible'
else:
    message = 'Not Eligible'

print(message)

# logical operators
has_high_income = True
has_good_credit = False
student = True

if (has_high_income and has_good_credit) and not student:
    print("Eligible for loan")
else:
    print("Not eligible for loan")

# short circuit evaluation
high_income = True
