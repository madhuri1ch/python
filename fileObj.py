
from os import read


with open('test.txt') as f:
    ''''content=f.readlines()
    for line in content:
        print(line)
    for line in f:
        print(line)'''
    ''''read_size=5
    content=f.read(read_size)
    while len(content)>0:
        print(content,end='*')
        content=f.read(read_size)'''
    with open('test_copy.txt','w') as wf:
        read_size=5
        content=f.read(read_size)
        while len(content)>0:
            wf.write(content)
            content=f.read(read_size)
        





#closing a file is taken care by content manager
#f.close()