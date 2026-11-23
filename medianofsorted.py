def sortedmedian(a,b):
    c=a+b
    c.sort()
    n=len(c)
    mid1=n//2
    mid2=mid1-1
    return int((c[mid1]+c[mid2])/2)

def getmedian(a,b):
    n=len(a)
    i,j,count=0,0,0
    m1,m2=-1,-1
    for count in range(n+1):
        m2=m1
        if i<n and j<n:
            if a[i]>b[j]:
                m1=b[j]
                j+=1
            else:
                m1=a[i]
                i+=1
        elif i<n:
            m1=a[i]
            i+=1
        else:
            m1=b[j]
            j+=1
    return int((m1+m2)/2)
a=[1,12,15,26,38]
b=[2,13,17,30,45]
print(sortedmedian(a,b))
print(getmedian(a,b))