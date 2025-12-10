global z
z = 3

def changeVar(z):
    z = 4
    print('z in function: ', z)

print('first global z: ', z)

if __name__ == '__main__':
    changeVar(z)
    print('2nd global z: ', z)