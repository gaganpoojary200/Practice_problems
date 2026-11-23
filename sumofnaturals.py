# def findsum(n):
#     sum=0
#     for i in range(1,n+1):
#         sum+=i
#     return sum
# if __name__=="__main__":
#     n=int(input("Enter a number:"))
#     print(findsum(n))


# def findsum(n):
#     if n==1:
#         return 1
#     return n+findsum(n-1)
# if __name__=="__main__":
#     n=int(input("Enter a number:"))
#     print(findsum(n))


def findsum(n):
    return n*(n+1)/2
if __name__=="__main__":
    n=int(input("Enter a number:"))
    print(findsum(n))