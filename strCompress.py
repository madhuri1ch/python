input='AAAABBBCCEEEEE'
#expected output=A4B3C2E5

def compress(s):
    l=len(s)
    r=""
    cnt=1
    i=1
    while i<l:
        if s[i]==s[i-1]:
            cnt+=1
        else:
            r=r+s[i-1]+str(cnt)
            cnt=1
        i+=1
    r=r+s[i-1]+str(cnt)
    return r 
print(compress(input))