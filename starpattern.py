n=3
def starpattern1(n):
    for i in range(n):
        print(" "*(n-i-1),end='')
        print("*"*(2*i+1),end='')
        print(" "*(n-i-1))

def starpattern2(n):
    for i in range(n):
        print("*"*(i+1))

starpattern2(n)

def starpattern3(n):
    for i in range(n):
        print("*")