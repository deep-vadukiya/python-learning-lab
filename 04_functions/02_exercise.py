# fizz buzz ...

# if the input is divisible by 3 it will return: fizz
# if the input is divisible by 5 it will return: buzz
# if the input is divisible by both 3 and 5 it will return: fizzbuzz
# if the input is not divisible by 3 or 5 it will return the input


def fizz_buzz(input):
    if input % 3 == 0 and input % 5 == 0:
        return "fizzbuzz"
    elif input % 3 == 0:
        return "fizz"
    elif input % 5 == 0:
        return "buzz"
    else:
        return input


print(fizz_buzz(15))  # fizzbuzz
print(fizz_buzz(9))  # fizz
print(fizz_buzz(10))  # buzz
print(fizz_buzz(7))  # 7
