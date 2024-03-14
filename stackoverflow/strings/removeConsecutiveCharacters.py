def solve( A, B):
        output=''
        i=0
        l=1
        n=len(A)
        while(i<(n-1)):
            output=output+(A[i])
            print(f' start of loop: output={output}')
            if A[i]==A[i+1]:
                l+=1
                #print(f'start={start}, end={end}')
            if (l)==B:
                output=output[:-(B-1)]
                print(f'output={output}')
                l=1
                i+=1
                print(i)
            i+=1
            print(i)
        return output
print(solve("aabbccd",2))