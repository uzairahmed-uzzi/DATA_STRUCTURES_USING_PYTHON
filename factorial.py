def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)

if __name__ == '__main__':
    i=True
    while(i==True):
        n=int(input("INPUT NUMBER TO FIND FACTORIAL: "))
        output=fact(n)
        print(f"FACTORIAL OF A GIVEN NUMBER {n} is {output}")
        conti=int(input("WANT TO EXIT?? PRESS 1: "))
        if conti==1:
            i=False
        else:
            i=True