def insertion(arr,k):
    for i in range(len(arr)):
        if arr[i]>=k:
            return i
    return len(arr)

def insertion1(arr,k):
    l,r=0,len(arr)-1
    while l<r:
        mid=(l+r)//2
        if arr[mid]==k:
            return mid
        elif arr[mid]>k:
            r=mid-1
        else:
            l=mid+1
    return l
arr=[1,2,3,5,6,7,9]
k=8
print(insertion1(arr,k))