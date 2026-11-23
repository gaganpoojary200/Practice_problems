def armstrong(n):
    num=str(n)
    order=len(num)
    output=0
    for i in num:
        output+=int(i)**order
    return output==n
if __name__=="__main__":
    print(armstrong(158))