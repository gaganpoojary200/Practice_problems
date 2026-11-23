# def countdigit(n):
#     count=0
#     while n!=0:
#         n=n//10
#         count+=1
#     return count

# def countdigit(n):
#     if n//10==0:
#         return 1
#     return 1+countdigit(n//10)

def countdigit(n):
    num=str(n)
    if num[0]=='-':
        return len(num)-1
    return len(num)
if __name__=="__main__":
    print(countdigit(567834))