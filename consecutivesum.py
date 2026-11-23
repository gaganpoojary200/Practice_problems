def consecutivesum(n):
    for i in range(1,n):
        sum=0
        for j in range(i,n):
            sum+=j
            if sum==n and j>i:
                return True
            if sum>n:
                break
    return False
if __name__=="__main__":
    n=int(input("n:"))
    print(consecutivesum(n))