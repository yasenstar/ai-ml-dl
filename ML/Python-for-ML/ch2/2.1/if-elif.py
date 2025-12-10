x = int(input("Input one integer: "))
if x < 0:
    print('negative')
elif x < 25:
    print('under 25')
elif x == 25:
    print("exactly 25")
else:
    print('over 25')