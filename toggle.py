def toggle(str):
    result=""
    for i in range(len(str)):
        ch=str[i]
        if ch.isupper():
            result+=ch.lower()
        else:
            result+=ch.upper()
    return result

str="geeKSForGeeKs"
print(toggle(str))
