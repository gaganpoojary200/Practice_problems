

# def findchar(s,ch):
#     # n=len(s)
#     # for i in range(n):
#     #     if s[i]==ch:
#     #         return i
#     # return -1
#     idx=s.find(ch)
#     return idx
# if __name__=="__main__":
#     s="geeksforgeeks"
#     ch='k'
#     print(findchar(s,ch))


# def findsubstring(str,substr):
#     n=len(str)
#     m=len(substr)
#     for i in range(n-m+1):
#         j=0
#         while j<m and str[i+j]==substr[j]:
#             j+=1
#         if j==m:
#             return i
#     return -1
# if __name__=="__main__":
#     str="geeksforgeeks"
#     substr="for"
#     print(findsubstring(str,substr))


# def insertchar(s,c,pos):
#     return s[:pos]+c+s[pos:]

# def insertchar1(s,c,pos):
#     res=""
#     for i in range(len(s)):
#         if i==pos:
#             res+=c
#         res+=s[i]
#     if pos>=len(s):
#         res+=c
#     return res
# def deletechar(s,c):
#     newstr=""
#     for char in s:
#         if char!=c:
#             newstr+=char
#     return newstr
# def deletechar1(s,pos):
#     return s[:pos]+s[pos+1:]
# if __name__=="__main__":
#     s='Geeks'
#     print(insertchar1(s,'f',5))
#     print(deletechar1(s,3))

# def samestring(s1,s2):
#     return s1==s2

# def samestring1(s1,s2):
#     if len(s1)!=len(s2):
#         return False
#     for i in range(len(s1)):
#         if s1[i]!=s2[i]:
#             return False
#     return True
# s1="hello"
# s2="hihello"
# print(samestring1(s1,s2))

# def stringconcat(s1,s2):
#     return s1+s2
# def stringconcat1(s1,s2):
#     res=""
#     for c in s1:
#         res+=c
#     for c in s2:
#         res+=c
#     return res
# s1="Hi "
# s2="hello"
# print(stringconcat1(s1,s2))

# def reversestring(s):
#     res=[]
#     for i in range(len(s)-1,-1,-1):
#         res.append(s[i])
#     return ''.join(res)
# def reversestring1(s):
#     return s[::-1]
# def reversestring2(s):
#     l=0
#     r=len(s)-1
#     s=list(s)
#     while l<r:
#         s[l],s[r]=s[r],s[l]
#         l+=1
#         r-=1
#     return ''.join(s)
# s="abcdef"
# print(reversestring2(s))


def palindrome(s):
    l=0
    r=len(s)-1
    while l<r:
        if s[l]!=s[r]:
            return False
        l+=1
        r-=1
    return True
def palindrome1(s,l,r):
    if l>=r:
        return True
    if s[l]!=s[r]:
        return False
    return palindrome1(s,l+1,r-1)
s="abba"
l=0
r=len(s)-1
print(palindrome1(s,l,r))