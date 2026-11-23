# def gcd(a,b):
#     if a==0 or b==0:
#         return max(a,b)
#     result=min(a,b)
#     while result>0:
#         if(a%result==0 and b%result==0):
#             break
#         result-=1
#     return result


# def gcd1(a,b):
#     if a==0 or b==0:
#         return max(a,b)
#     if a==b:
#         return a
#     if a>b:
#         return gcd1(a-b,b)
#     return gcd1(a,b-a)

import math
def gcd(a,b):
    return math.gcd(a,b)

if __name__=="__main__":
    print(gcd(20,28))