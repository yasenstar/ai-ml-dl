def changeMe(mylist):
    mylist.append([1,2,3,4])
    print("Value inside the function: ", mylist)
    return

mylist = [10,20,30]
changeMe(mylist)
print("Values outside the functions: ", mylist)