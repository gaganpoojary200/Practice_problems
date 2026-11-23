def palindrome(n):
    reverse=0
    temp=n
    while temp!=0:
        reverse=reverse*10+(temp%10)
        temp//=10
    return reverse==n


def palindrome1(n):
    s=str(n)
    return s==s[::-1]
if __name__=="__main__":
    print(palindrome(123421))
    print(palindrome1(123454321))