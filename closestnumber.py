# def closestno(n,m):
#     closest=0
#     min_diff=float('inf')
#     for i in range(n-abs(m),n+abs(m)+1):
#         if i%m==0:
#             diff=abs(n-i)
#             if diff<min_diff or (diff==min_diff and abs(i)>abs(closest)):
#                 closest=i
#                 min_diff=diff
#     return closest
# if __name__=="__main__":
#     n=int(input("n:"))
#     m=int(input("m:"))
#     print(closestno(n,m))



def closestno(n,m):
    q=int(n/m)
    n1=m*q
    if ((n*m)>0):
        n2=m*(q+1)
    else:
        n2=m*(q-1)

    if(abs(n-n1)<abs(n-n2)):
        return n1
    return n2
if __name__=="__main__":
    n=int(input("n:"))
    m=int(input("m:"))
    print(closestno(n,m))