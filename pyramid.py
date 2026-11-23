def pyramid(n):
    for i in range(1,n+1):
        print(" "*(n-i),end="")
        print("*"*(2*i-1))

def pyramid1(n):
    for i in range(1,n+1):
        for j in range(i):
            print("*",end=' ')
        print()

def pyramid2(n):
    for i in range(n+1,0,-1):
        for j in range(i):
            print("*",end=' ')
        print()

def pyramid3(n):
    for i in range(n,0,-1):
        for j in range(i):
            print(" ",end=' ')
        print("*"*(n-i+1),end=' ')
        print()

if __name__=="__main__":
    pyramid3(5)