maxPower = 64
maxCount = 4

def pwr(num):
    prod = 1
    for n in range(1,maxPower+1):
        prod = prod*num
        if n < maxPower:
            continue
        print(num, 'to the power', n, 'equals', prod)
    print('-'*15)

for num in range(1, maxCount+1):
    pwr(num)