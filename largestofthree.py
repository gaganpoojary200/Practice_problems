a,b,c=map(int,input("Enter three numbers:").split())
if a>b and a>c:
    print("a is largest")
elif b>c:
    print("b is largest")
else:
    print("c is largest")