x = input("Please input first string: ")
y = input("Please input 2nd string: ")
print(x, '\n', y)

if (x == y):
    print('x and y: identical')
elif (x.lower() == y.lower()):
    print('x and y: case insensitive match')
else:
    print('x and y: different')