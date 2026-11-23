def reomvespace(str):
    str=str.replace(" ","")
    return str

def reomvespace1(str):
    s=list(str)
    i=0
    n=len(s)
    while i<n:
        if s[i]==" ":
            for j in range(i,n-1):
                s[j]=s[j+1]
            n-=1
            i-=1
        i+=1
    return "".join(s[:n])
str="gee k s fo r ge eks"
print(reomvespace1(str))