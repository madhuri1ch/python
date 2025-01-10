"""iven an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order."""

def twoSum( nums, target):

        
        l=len(nums)

        if l==0 :
                return None
        #print(nums)
        
        for i in range(l-1):
            j=i+1
            while j<l:
                   if nums[i]+nums[j]==target:
                          return [i,j]
                   else:
                          j+=1


print(twoSum([-1,-2,-3,-4,-5],-8))