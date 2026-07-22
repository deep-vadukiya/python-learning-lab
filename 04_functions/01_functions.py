#

def greet(first_name, last_name):
    print(
        f"Hello {first_name} {last_name}, welcome to the Python learning lab ...!")
    print("This is a simple function that greets the user ...")


# adding 2 line breaks is recommended after function definition and function call for better readability
# greet("John", "Doe")


# function with return value and with default argument value
def increment(number, by=1):
    return number + by


# print(increment(5, by=2))  # Output: 7
# print(increment(5))  # Output: 6


# multiple arguments
def multiply(*numbers):
    # print(numbers)
    total = 1
    for number in numbers:
        # print(number)
        total *= number
        return total


print('start')
print(multiply(2, 3, 4, 5,))


##
def save_user(**user):
    print(user)
    print(user['name'])


# save_user(id=1, name="John", age=30, email="johndoe@demo.com")
