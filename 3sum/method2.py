def threeSum( nums):
        result=[]
        l=len(nums)
        if len(nums)<3:
            return result
        nums.sort()
        print(nums)
        for i in range(l-1):
            j=i+1
            k=l-1
            while(j<k):
                print(f'nums={nums[i]},{nums[j]},{nums[k]}')
                sum=nums[i]+nums[j]+nums[k]
                print(f'sum={sum}')
                if sum==0:
                    o=[nums[i],nums[j],nums[k]]
                    print(f'o={o}')
                   # o.sort()
                    print(f'result before {result}, {o}')
                    if o not in result:
                        print('inside')
                        result.append(o)
                    j+=1
                    k-=1
                    
                    print(f'result:{result}')
                    
                elif (sum>0) :
                    k-=1
                else :
                    j+=1

        return (result)

print(threeSum([-1,0,1,2,-1,-4]))