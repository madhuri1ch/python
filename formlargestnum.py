

A = [ 472, 663, 964, 722, 485, 852, 635, 4, 368, 676, 319, 412 ]
def largestNumber( A):
        l=len(A)
        
        A.sort(reverse = True)
        print(A)
        number=A[0]
        for i in range(1,l):
            print("num: {}".format(number))
    
            before=str(A[i])+str(number)
            after=str(number)+str(A[i])
            print("before{} , after:{} ".format(before,after))
            number=max(int(before),int(after))
     
        return number

print(largestNumber(A))
        