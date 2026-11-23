def main():
    s="geeksforgeeks"
    c='e'
    s=s.replace(c,'')
    print(s)

def remove(str,c):
    j=0
    s=list(str)
    for i in range(len(s)):
        if s[i]!=c:
            s[j]=s[i]
            j+=1
    return ''.join(s[:j])

str='geeksforgeeks'
c=input()
print(remove(str,c))
