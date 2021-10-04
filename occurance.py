a=[1,"1",'a',1]
d={}
for i in a:
    if i in d:
        d[i]=d[i]+1
    else:
        d[i]=1

print(d)