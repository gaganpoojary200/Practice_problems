def primefactor(n):
    ans=[]
    for i in range(2,n):
        while n%i==0 and n>0:
            ans.append(i)
            n=n//i
    return ans
if __name__=="__main__":
    print(primefactor(18))