a=15
def fonk():
    a=25
    print(a)
fonk()
print(a)

def fonk2():
    global a
    a=35
    print(a)
fonk2()
print(a)