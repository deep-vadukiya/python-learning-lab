# for loop ...

# for number in range(1, 10, 2):
#     print('Attempt', number, (number) * '.')
#     print('Sending a message ...')

# for else loop ...
successful = True
for number in range(1, 4):
    print('Attempt')
    if successful:
        print('Successful')
        break
else:
    print('Attempted 3 times and failed')

# if you never break out of the loop, the else block will be executed. If you break out of the loop, the else block will not be executed.

# Nested loops ...
# for x in range(5):
#     for y in range(3):
    # print(f'({x}, {y})')

# iterables ...
print(type(5))
print(type(range(5)))

for x in 'Python':
    print(x)


for x in [1, 2, 3, 4, 5]:
    print(x)
