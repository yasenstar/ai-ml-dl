import sys
try:
    f = open('myfile.txt')
    for lines in f:
        s = f.readline()
        print(s)
        i = int(s.strip())
except IOError as err:
    print("I/O error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_into()[0])
    raise