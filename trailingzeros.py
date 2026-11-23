def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    return fact
def trailingzeros(n):
    fact=factorial(n)
    count=0
    while fact%10==0:
        count+=1
        fact//=10
    return count
if __name__=="__main__":
    n=100
    print(trailingzeros(n))