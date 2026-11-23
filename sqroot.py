# def sqroot(n):
#     l=0
#     r=n
#     res=1
#     while l<r:
#         mid=(l+r)//2
#         if mid*mid<=n:
#             res=mid
#             l=mid+1
#         else:
#             r=mid-1
#     return res
# n=11
# print(sqroot(n))



# arr=[1,2,3,4,5]
# product=1
# for i in range(len(arr)):
#     product*=arr[i]
# lst=[]
# for i in range(len(arr)):
#     lst.append(int(product/arr[i]))
# print(lst)


arr1=[1,2,3,4]
arr2=[8,7,6,5]
# i=0
# j=len(arr2)-1
# k=0
# arr=[]*(len(arr1)+len(arr2))
# while i<len(arr1) and j>=0:
#     if arr1[i]<=arr2[j]:
#         arr.append(arr1[i])
#         i+=1
#     else:
#         arr.append(arr2[j])
#         j-=1
#     k+=1
# while i<len(arr1):
#     arr.append(arr1[i])
#     i+=1
# while j>=0:
#     arr.append(arr2[j])
#     j-=1
# print(arr)
