'''
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

'''
#ALGO

'''
remove the duplicate and sort the array

intialize with max length=1, start=index of first element and templength=1
if the difference betwwn current and next lement is 1 then 
    increment the temp length
else:
    if maxlength is less than templength then 
        max length=temp length

    and assign 
    start=index of next element as it could be start of a new sequence
    l=1
return max of (maxlength, l)

'''

def longestConsecutive( nums) -> int:
        nums=set(nums)
        nums=list(nums)
        nums.sort()
        if len(nums)==0:
            return 0
        maxlength=1
        finalstart=0
        finalend=0
        start=0
        l=1
        print(nums)
        for i in range(len(nums)-1):
            print(f'diff={nums[i+1]-nums[i]}')
            if nums[i+1]-nums[i]!=1:
                if maxlength<l:
                    print(f'i-start={i-start}')
                    finalstart=start
                    finalend=i
                    maxlength=l
                    print(f'finalstart={finalstart},finalend={finalend},maxlength={maxlength}')
                    
                    print(f'start={i+1}')
                start=i+1
                l=1
            elif nums[i+1]-nums[i]==1:
                 l+=1
                 
                
        return max(maxlength,l)
print(longestConsecutive([-4, -3, -2, -1, 1, 2, 3, 4, 6, 7, 8, 9]))

