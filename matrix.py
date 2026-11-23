# rows=3
# cols=3
# rows,cols=(3,3)
# arr=[[0]*cols]*rows
# arr=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# print(arr[0][2])
# for row in arr:
#     for x in row:
#         print(x,end=' ')
#     print()
# def search(arr,x):
#     rows,cols=len(arr),len(arr[0])
#     for i in range(rows):
#         for j in range(cols):
#             if arr[i][j]==x:
#                 return (i,j)
#     return False
# print(search(arr,10))


# def issorted(arr):
#     # n=len(arr)
#     # for i in range(1,n):
#     #     if arr[i-1]>arr[i]:
#     #         return False
#     # return True
#     return arr==sorted(arr)
# if __name__=="__main__":
#     ar=[10,20,30,40,50]
#     print(issorted(ar))


# def reverse(arr,n):
#     temp=[0]*n
#     for i in range(n):
#         temp[i]=arr[n-i-1]
#     return temp

# def reverse1(arr):
#     l=0
#     r=len(arr)-1
#     while l<r:
#         arr[l],arr[r]=arr[r],arr[l]
#         l+=1
#         r-=1
#     return arr

# def reverse2(arr):
#     arr.reverse()

# def reverse3(arr,n):
#     for i in range(n//2):
#         temp=arr[i]
#         arr[i]=arr[n-i-1]
#         arr[n-i-1]=temp
#     return arr
# arr=[1,5,2,6,3,7]
# n=len(arr)
# print(reverse3(arr,n))
# print(" ".join(map(str,arr)))


# arr=[1,2,3,4,5,6,7,8,9]
# k=4
# print(k%len(arr))
# arr.reverse()
# arr[:k]=reversed(arr[:k])
# arr[k:]=reversed(arr[k:])
# print(arr)

# def subarray(arr):
#     n=len(arr)
#     for i in range(n):
#         for j in range(i,n):
#             for k in range(i,j+1):
#                 print(arr[k],end=' ')
#             print()
# arr=[1,2,3,4,5]
# subarray(arr)


def majority_element(arr):
    n=len(arr)
    for i in range(n):
        count=0
        for j in range(n):
            if arr[i]==arr[j]:
                count+=1
        if count>n//2:
            return arr[i]
    return -1
arr=[1,2,1,1,1,2,3,5,1,2,2,2,2]
print(majority_element(arr))