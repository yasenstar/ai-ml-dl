userInput = input("Enter something:")
try:
    x = 0 + eval(userInput)
    print('You entered the number:', userInput)
except:
    print(userInput, 'is a string')