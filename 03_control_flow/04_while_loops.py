# while loops ...

# number = 100
# while number > 0:
#     print(number)
#     number //= 2

command = ""
# while command.lower() != "quit":
#     command = input(">")
#     print("ECHO", command)

# infinite loops ...

count = 0
for number in range(1, 10):
    if number % 2 == 0:
        count += 1
        print("Even number:", number)

print("Count of even numbers:", count)
