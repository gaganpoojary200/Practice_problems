def upperbound(arr,target):
    n=len(arr)
    for i in range(n):
        if arr[i]>target:
            return i
    return n


def upperbound1(arr,target):
    l=0
    r=len(arr)-1
    res=len(arr)
    while l<r:
        mid=(l+r)//2
        if arr[mid]>target:
            res=mid
            r=mid-1
        else:
            l=mid+1
    return res
arr=[1,2,3,4,7,9]
target=6
print(lowerbound(arr,target))